# FastAPI RAG Document QA System

A Retrieval-Augmented Generation (RAG) based document question-answering system built using **FastAPI**, **embeddings**, and **semantic search**.
Upload documents and ask questions — the system retrieves relevant context and generates accurate answers.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Semantic search using embeddings
* 🤖 Retrieval-Augmented Generation (RAG)
* ⚡ FastAPI backend
* 🌐 Simple UI for asking questions
* 📚 Multi-document support
* 🧠 Context-aware answers
* 🗂️ Automatic document chunking

---

## 🏗️ Project Structure

```
rag-fastapi/
│
├── main.py              # FastAPI app
├── rag.py               # RAG pipeline logic
├── requirements.txt
│
├── templates/
│   └── index.html       # UI
│
├── uploads/             # uploaded docs (empty in repo)
│   └── .gitkeep
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repo

```
git clone https://github.com/nyasalohiya/rag-fastapi.git
cd rag-fastapi
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Server

```
uvicorn main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 How It Works

1. Upload PDF document
2. Text extracted and chunked
3. Embeddings generated
4. Stored in vector format
5. User asks question
6. Relevant chunks retrieved
7. LLM generates answer

---

## 📌 Example Use Cases

* Pharma SOP QA
* Research paper assistant
* Personal knowledge base
* Document chatbot
* Compliance document search
* Study material assistant

---

## 🛠️ Tech Stack

* FastAPI
* Python
* Sentence Transformers / Embeddings
* PyPDF2
* HTML (UI)
* Uvicorn

---

## 📈 Future Improvements

* Add vector database (FAISS / Chroma)
* Multi-file upload
* Chat history
* Streaming responses
* Authentication
* Docker support

---

## 👩‍💻 Author

Nyasa Lohiya

---
