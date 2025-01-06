from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
import httpx
import os
from uuid import uuid4
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
import numpy as np
from pydantic import BaseModel


class URLRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    chat_id: str
    question: str


app = FastAPI()
data_dir = "./data"
os.makedirs(data_dir, exist_ok=True)
model = SentenceTransformer("all-MiniLM-L6-v2")


@app.post("/process_url")
async def process_url(request: URLRequest):
    try:
        # URL = https://www.toppr.com/guides/speech-for-students/apj-abdul-kalam-speech/
        url = request.url
        response = httpx.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join(soup.stripped_strings)
        chat_id = str(uuid4())
        with open(f"{data_dir}/{chat_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        return {
            "chat_id": chat_id,
            "message": "URL content processed and stored successfully.",
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/process_pdf")
async def process_pdf(file: UploadFile):
    try:
        chat_id = str(uuid4())
        text = ""
        # file_path = "./Developer_Round_1.pdf"
        pdf_reader = PdfReader(file.file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        cleaned_text = " ".join(text.split())
        with open(f"{data_dir}/{chat_id}.txt", "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        return {
            "chat_id": chat_id,
            "message": "PDF content processed and stored successfully.",
        }
    except Exception as e:
         # Print the full stack trace
        print(f"An error occurred: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        chat_id = request.chat_id
        question = request.question
        file_path = f"{data_dir}/{chat_id}.txt"
        if not os.path.exists(file_path):
            return JSONResponse(
                content={"error": "Chat ID not found."}, status_code=404
            )

        with open(file_path, "r",encoding="utf-8") as f:
            content = f.read()

        # Embedding generation
        content_embedding = model.encode(content, convert_to_tensor=True)
        question_embedding = model.encode(question, convert_to_tensor=True)

        # Cosine similarity
        similarity = util.pytorch_cos_sim(question_embedding, content_embedding)
        if similarity.item() > 0.2:  # Threshold for relevance
            return {"response": content}
        else:
            return {"response": "Sorry, I couldn't find a relevant answer."}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
