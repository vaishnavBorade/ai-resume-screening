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
- ✅ Click on a candidate to see full resume insights

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

🚀 Run Locally
```bash
uvicorn main:app --reload
```
Now the backend will be live at: http://127.0.0.1:8000
You can test endpoints at the interactive docs: http://127.0.0.1:8000/docs

## 🎨 Frontend (Next.js + Tailwind CSS + ShadCN)

### 🔧 Tech Stack

- **Next.js 15 (App Router)**
- **Tailwind CSS** – Utility-first styling
- **ShadCN/UI** – Pre-styled accessible components
- **TypeScript** – For type safety
- **Sonner** – For beautiful toast notifications

---

### 📦 Installation

```bash
cd frontend
npm install
```

Make sure to set the backend URL in .env:
```bash
NEXT_PUBLIC_BACKEND_URL=https://your-backend-url.onrender.com
```
Replace your-backend-url with the actual hosted backend link.

🚀 Run Locally
```bash
npm run dev
```
Open your browser and go to: http://localhost:3000
You’ll see the Resume Ranking UI.


## 🚀 Deployment

### 🟢 Backend Deployment (Render)

1. Push your `/backend` code to GitHub.
2. Go to [Render.com](https://render.com) → New Web Service.
3. Connect your GitHub repo.
4. Set environment:
   - Runtime: Python 3.10+
   - Start command: `uvicorn main:app --host=0.0.0.0 --port=10000`
5. Add environment variables:
   - `OPENROUTER_API_KEY`
   - `OCR_API_KEY`
6. Expose port: **10000**
7. Click Deploy

> Backend will be available at `https://your-backend-url.onrender.com`

---

### 🟢 Frontend Deployment (Vercel / Render)

1. Push your `/frontend` code to GitHub.
2. On [Vercel](https://vercel.com) or Render:
   - Connect GitHub repo
   - Set root directory to `/frontend`
3. Set Environment Variable:

```env
NEXT_PUBLIC_BACKEND_URL=https://your-backend-url.onrender.com
```
4. Click Deploy.