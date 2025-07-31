# 🧠 AI Resume Screening System

An AI-powered web application that automates the resume screening process by ranking candidates based on how well their resumes match a given job description. Built with FastAPI, Sentence Transformers, FAISS, and Next.js (App Router).

---

## ✨ Features

* 📄 **Upload multiple resumes** in PDF format
* 📌 **Paste a job description** to match candidates
* 🧠 **Semantic ranking** using sentence embeddings
* ⚡ **Fast similarity search** using FAISS
* 🔍 **LLM-powered explanations** for top candidates
* 💻 **Full-stack**: FastAPI backend + Next.js frontend
* ☁️ **Deployed on [Render](https://render.com)**

---

## 📁 Project Structure

ai-resume-screening/
│
├── backend/            # FastAPI backend
│   ├── main.py
│   ├── parser.py       # PDF + OCR text extraction
│   ├── ranker.py       # Embedding, FAISS, ranking
│   ├── requirements.txt
│   └── .env
│
├── frontend/           # Next.js frontend
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── .env.local
│   ├── tailwind.config.ts
│   └── ...
│
├── README.md
└── ...


---

## ⚙️ Backend (FastAPI)

### 🔧 Tech Stack

* Python 3.10+
* FastAPI
* SentenceTransformers
* FAISS
* OpenAI or Mistral LLM (optional)
* OCR.space API (fallback for scanned resumes)

### 📦 Setup Locally

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
Create a .env file:

Ini, TOML

OCR_API_KEY=your_ocr_space_api_key
OPENAI_API_KEY=your_openai_key   # optional
🚀 Run the Server
Bash

uvicorn main:app --reload
API will be available at http://localhost:8000

🎨 Frontend (Next.js)
🔧 Tech Stack
Next.js 15 (App Router)

Tailwind CSS

TypeScript

ShadCN UI

Sonner for toasts

📦 Setup Locally
Bash

cd frontend
npm install
Create a .env.local file:

Ini, TOML

NEXT_PUBLIC_BACKEND_URL=[https://your-backend-url.onrender.com](https://your-backend-url.onrender.com)
🚀 Run the Frontend
Bash

npm run dev
Visit: http://localhost:3000

☁️ Deployment
✅ Backend on Render
Create a new Web Service

Language: Python

Start command: uvicorn main:app --host=0.0.0.0 --port=10000

Expose Port: 10000

Add environment variables:

OCR_API_KEY

OPENAI_API_KEY (optional)

✅ Frontend on Vercel / Render
Framework: Next.js

Build command: npm run build

Output directory: .next

Add environment variable:

NEXT_PUBLIC_BACKEND_URL=https://your-backend-url.onrender.com

🔒 Environment Variables
Variable Name	Description
OCR_API_KEY	OCR.space API key for scanned PDFs
OPENAI_API_KEY	OpenAI/Mistral API key (optional)
NEXT_PUBLIC_BACKEND_URL	Backend endpoint for the frontend to connect

Export to Sheets
📸 Screenshots
You can add screenshots here of:

Resume upload form

Job description input

Ranked results with explanations

Candidate modal view

💡 Future Improvements
Add authentication (admin dashboard)

Store results history

Add support for DOCX/image resumes

Export ranked candidates as CSV

Add resume deduplication logic

Dashboard to view past results

🧑‍💻 Author
Made with ❤️ by Vaishnav Borade

📜 License
This project is licensed under the MIT License.