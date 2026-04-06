import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="Your_gemini_api_key")
model = genai.GenerativeModel("gemini-2.5-flash")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Global FAISS index + document storage
dimension = 384  # all-MiniLM-L6-v2 embedding size
index = faiss.IndexFlatL2(dimension)
documents = []


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def add_document_to_db(file_path):
    global documents

    text = read_pdf(file_path)

    # simple chunking
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    embeddings = embedding_model.encode(chunks)

    index.add(np.array(embeddings).astype("float32"))
    documents.extend(chunks)


def query_rag(question):
    global documents

    if len(documents) == 0:
        return "No document uploaded yet. Please upload a PDF first."

    question_embedding = embedding_model.encode([question])
    D, I = index.search(
        np.array(question_embedding).astype("float32"),
        k=min(3, len(documents))
    )

    context = ""

    for idx in I[0]:
        if 0 <= idx < len(documents):
            context += documents[idx] + " "

    if context.strip() == "":
        return "Could not find relevant information in the document."

    prompt = f"""
    Answer based only on the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text
