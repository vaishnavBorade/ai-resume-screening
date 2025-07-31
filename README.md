# 🧠 AI Resume Screening System

This is a full-stack AI-powered resume screening web application. It allows recruiters to upload multiple resumes (PDFs), input a job description, and receive ranked candidates based on semantic similarity. It uses Sentence Transformers for embeddings, FAISS for vector similarity search, and OpenAI/Mistral for LLM-based explanations.

## 🌐 Live Demo

- **Frontend**: [https://your-frontend-url.onrender.com](https://your-frontend-url.onrender.com)
- **Backend API**: [https://your-backend-url.onrender.com](https://your-backend-url.onrender.com)

## 📁 Project Structure

ai-resume-screening/
├── backend/ # FastAPI backend with AI logic
├── frontend/ # Next.js frontend for uploading and viewing results
└── README.md


## ✨ Features

- ✅ Upload multiple resume PDFs
- ✅ Paste job description
- ✅ AI-powered candidate ranking
- ✅ Semantic search using Sentence Transformers + FAISS
- ✅ LLM-based explanations for match score
- ✅ Clean UI with dark/light support using Shadcn + Tailwind
- ✅ Fully deployed on Render
