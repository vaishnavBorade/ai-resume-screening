# 🧠 AI Resume Screening System

This is a full-stack AI-powered resume screening web application. It allows recruiters to upload multiple resumes (PDFs), input a job description, and receive ranked candidates based on semantic similarity. It uses Sentence Transformers for embeddings, FAISS for vector similarity search, and OpenAI/Mistral for LLM-based explanations.

## 🌐 Live Demo

- **Frontend**: [https://your-frontend-url.onrender.com](https://your-frontend-url.onrender.com)
- **Backend API**: [https://your-backend-url.onrender.com](https://your-backend-url.onrender.com)

## ✨ Features

- ✅ Upload multiple resume PDFs
- ✅ Paste job description
- ✅ AI-powered candidate ranking
- ✅ Semantic search using Sentence Transformers + FAISS
- ✅ LLM-based explanations for match score
- ✅ Clean UI with dark/light support using Shadcn + Tailwind
- ✅ Fully deployed on Render

## 🧠 Backend (FastAPI + FAISS + Transformers)

### 🔧 Tech Stack
- **FastAPI** – For building RESTful APIs
- **FAISS** – For fast similarity search over embeddings
- **Sentence Transformers** – For generating vector embeddings of resumes & job descriptions
- **PyPDF2 / OCR.Space API** – For extracting text from PDF resumes
- **OpenRouter (Mistral / GPT-4 / etc.)** – For generating AI-based match explanations
- **Redis / SQLite** – For caching embeddings to avoid recomputation

---

### 📦 Installation

```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

Create a .env file inside the backend/ folder with:
```bash
OPENROUTER_API_KEY=your_openrouter_key
OCR_API_KEY=your_ocr_space_api_key
```
🔑 Get an OpenRouter key from https://openrouter.ai.
🧾 Get a free OCR key from https://ocr.space/OCRAPI.