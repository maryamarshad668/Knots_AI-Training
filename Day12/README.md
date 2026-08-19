# AI FAQ Assistant

A simple Retrieval-Augmented Generation application that answers questions using a custom knowledge base.

## Project Objective

The goal of this project is to build a simple Retrieval-Augmented Generation (RAG) based FAQ assistant.

The assistant uses a custom knowledge base as its source of information. Instead of relying only on the knowledge stored inside the language model, the application retrieves relevant information from the knowledge base and provides it to Gemini as context.

The assistant is designed to answer only from the available knowledge base and return a fallback response when the required information is not available.

## Features

- Text knowledge base
- Text chunking
- Sentence Transformer embeddings
- FAISS vector search
- Similarity-based retrieval
- Gemini API integration
- Context-based answers
- Fallback when information is unavailable

## Project Structure

```text
ai-faq-assistant/
│
├── app.py
├── knowledge.txt
├── embeddings.py
├── vectorstore.py
├── rag.py
├── requirements.txt
└── README.md
```

## How RAG Works

RAG stands for Retrieval-Augmented Generation.

The system combines two main processes:

1. Retrieval
2. Generation

During retrieval, the user's question is converted into an embedding and compared with the embeddings of the stored document chunks. FAISS finds the most similar chunks.

During generation, the retrieved chunks are added to the prompt and sent to the Gemini API. Gemini then generates an answer using only the provided context.

## RAG Pipeline

│
├── knowledge.txt
├── Text Chunking
├── Sentence Transformers
├── Embeddings
├── FAISS
├── Relevant Context
└── Similarity Search
├── Gemini API
├── Answer

## Technologies Used
## Python

Python is used as the main programming language for implementing the complete RAG pipeline.

## Sentence Transformers

Sentence Transformers are used to convert text chunks and user questions into numerical vector representations called embeddings.

## The project uses:

all-MiniLM-L6-v2
## FAISS

FAISS is used as the vector database for storing embeddings and performing similarity searches.

FAISS helps find the document chunks that are most relevant to the user's question.

## Gemini API

The Gemini API is used as the Large Language Model.

Gemini receives the user's question together with the retrieved context and generates the final response.

## Learning Outcomes

After completing this project, the following concepts are demonstrated:

-Understanding of RAG
-Document processing
-Text chunking
-Semantic embeddings
-Vector databases
-FAISS similarity search
-Prompt augmentation
-Gemini API integration
-Modular Python development
-Knowledge-grounded generation
-Handling unavailable information