
# Backend Application With FastAPI

This project is to build a backend service with FastAPI that provides three main APIs:
1. Process Web URL API: 
 - Scrapes content from a given URL.
 - Stores the cleaned content and associates it with a unique chat_id.
2. Process PDF Document API
 - Extracts text from the uploaded PDF document.
 - Cleans the text (removing extra spaces, line breaks,etc.).
 - Stores the cleaned text and associates it with a unique chat_id.
3. ChatAPI
 - Uses embeddings to convert both the stored content and the user's query into vector representations.
 - Finds the most relevant sections of the stored content by comparing the query's embeddings with the stored content's embeddings (using cosine similarity).
 - Returns the most relevant response based on the comparison.

## API Reference

#### 1. Process Web URL API

```http
  POST /process_url
```

| Request Body | Type     | Response              |
| :-------- | :------- | :------------------------- |
| `"url":"https://example.com"` | `raw` | "chat_id": "unique_chat_id","message":"URL content processed and stored successfully."|

#### 2. Process PDF Document API

```http
  POST /process_pdf
```

| Request Body | Type     | Response                      |
| :-------- | :------- | :-------------------------------- |
| `form-data with the PDF file uploaded`      | `form-data` | "chat_id":"unique_chat_id","message":"PDF content processed and stored successfully." |

#### 3. ChatAPI
```http
  POST /chat
```

| Request Body | Type     | Response                      |
| :-------- | :------- | :-------------------------------- |
| `"chat_id":"unique_chat_id","question":"What is the main idea of the document?"`     | `raw` | "response":"The main idea of the document is..." |








## Installation

The code is written in python.Install the required libraries (FastAPI, uvicorn, beautifulsoup4, httpx, PyPDF2, sentence-transformers, and numpy).
To install the required packages and libraries, run this command in the project directory.Ensuring you have the latest version of pip.

```bash
 pip install -r requirements.txt
```


    
## Deployment

To deploy the project:

1. Build the Docker Image:
```bash
 docker build -t fastapi-service .
```

2. Run the container:
```bash
  docker run -d -p 8000:8000 fastapi-service
```

3. Access Your Application

Open a browser and navigate to:
```bash
  http://localhost:8000/docs
```

## Directory Structure

```bash
 project/
│
├── main.py          # FastAPI application
├── requirements.txt # Dependencies
├── Dockerfile       # Docker configuration
└── data/            # Directory for storing processed data
```
## Description

This repository contains a FastAPI application that provides three main APIs:

1. Process Web URL API
Scrapes the content from a given URL, cleans it, and stores it for future reference.

2. Process PDF Document API
Extracts text from an uploaded PDF document, processes the text, and stores it.

3. Chat API
Allows users to query the processed content (from either a URL or PDF) using a chat interface. The API uses embeddings and cosine similarity to find relevant responses to user queries.

To implementation the described system using FastAPI, integrated with Docker for deployment. We'll handle the following:

Dependencies: Install the required libraries (FastAPI, uvicorn, beautifulsoup4, httpx, PyPDF2, sentence-transformers, and numpy).

Structure: FastAPI app with three endpoints (/process_url, /process_pdf, and /chat).

Embedding Search: Use sentence-transformers for embedding generation and cosine similarity for search.

Dockerization: Provide a Dockerfile for deployment.
## Key Features

- Web Scraping: Scrapes and cleans HTML content from any provided URL.

 - PDF Parsing: Extracts text from PDF files and formats it for efficient storage and retrieval.

 - Chat Functionality: Supports natural language queries using sentence embeddings via the SentenceTransformer model.
 - Persistent Storage: Saves processed content locally, associated with a unique chat_id for reference.

 - Dockerized Deployment: The application is containerized for easy deployment.
## Technologies Used
Technologies Used are

 - FastAPI: For building the backend APIs.

 - BeautifulSoup: For web scraping.

 - PyPDF2: For extracting text from PDF files.

 - Sentence Transformers: For creating embeddings and finding semantic similarity.

 - Docker: For containerization and easy deployment.