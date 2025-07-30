from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from parser import extract_text_from_pdf
from embedder import get_embedding
from scorer import build_faiss_index, search_top_k
from llm import explain_match
import re
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/api/rank")
async def rank_resumes(files: list[UploadFile] = File(...), job_description: str = Form(...)):
    unique_resumes = OrderedDict()

    # Step 1: Deduplicate by filename and extract text
    for file in files:
        if file.filename not in unique_resumes:
            content = await file.read()
            unique_resumes[file.filename] = extract_text_from_pdf(content)

    # Step 2: Generate embeddings in parallel
    filenames = list(unique_resumes.keys())
    texts = list(unique_resumes.values())

    with ThreadPoolExecutor() as executor:
        embeddings = list(executor.map(get_embedding, texts))

    resumes = list(zip(filenames, texts))

    # Step 3: Build index and find top matches
    job_vec = get_embedding(job_description)
    index = build_faiss_index(embeddings)
    idxs, scores = search_top_k(index, job_vec, k=10)

    # Step 4: Score and explain for confident matches
    results = []
    seen_names = set()
    CONFIDENCE_THRESHOLD = 0.6  # Cosine similarity threshold (0 to 1)

    for i, sim_score in zip(idxs, scores):
        if sim_score < CONFIDENCE_THRESHOLD:
            continue  # Skip low-confidence matches

        name, text = resumes[i]
        if name in seen_names:
            continue
        seen_names.add(name)

        score_exp = explain_match(job_description, text)
        score_match = re.search(r"(?i)(score|match score)[^\d]*?(\d{1,3})", score_exp)
        score = int(score_match.group(2)) if score_match else 0
        explanation = score_exp.replace(score_match.group(0), "").strip() if score_match else score_exp

        results.append({
            "name": name,
            "score": score,
            "explanation": explanation
        })

        if len(results) >= 10:
            break

    # Step 5: Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results}
