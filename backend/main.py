from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from parser import extract_text_from_pdf
from embedder import get_embedding
from scorer import build_faiss_index, search_top_k
from llm import explain_match
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.post("/api/rank")
async def rank_resumes(
    files: list[UploadFile] = File(...), 
    job_description: str = Form(...)
):
    resume_map = {}
    embeddings = []

    # Deduplicate resumes by filename
    for file in files:
        if file.filename in resume_map:
            continue  # skip duplicates
        content = await file.read()
        text = extract_text_from_pdf(content)
        emb = get_embedding(text)
        resume_map[file.filename] = text
        embeddings.append(emb)

    resumes = list(resume_map.items())  # [(filename, text), ...]
    job_vec = get_embedding(job_description)
    index = build_faiss_index(embeddings)
    idxs, _ = search_top_k(index, job_vec, k=min(10, len(resumes)))

    results = []
    for i in idxs:
        filename, resume_text = resumes[i]
        score_exp = explain_match(job_description, resume_text)

        # Extract score from LLM response
        score_match = re.search(r"(?i)(score|match score)[^\d]*?(\d{1,3})", score_exp)
        score = int(score_match.group(2)) if score_match else 0

        if score_match:
            score_line = score_match.group(0)
            explanation = score_exp.replace(score_line, "").strip()
        else:
            explanation = score_exp

        results.append({
            "name": filename,
            "score": score,
            "explanation": explanation
        })

    # ✅ Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # ✅ Limit to top 10
    return {"results": results[:10]}
