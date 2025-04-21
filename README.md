## RAG Chatbot Assistant – LangChain + OpenAI + FAISS (Multi-Turn Q&A)

This project is a **full-stack Retrieval-Augmented Generation (RAG) chatbot assistant**, built with ***LangChain***, ***FAISS***, ***OpenAI API***, ***Flask***, ***Streamlit***, and ***Docker***.

It demonstrates how to build a modular, conversational LLM-based Q&A system over domain-specific documents — in this case, summaries of rental buildings in the NYC metropolitan area (based on places I or friends have lived in or visited).

---

### Key Features:

- 📄 Document ingestion, chunking, and semantic embedding via OpenAI's embedding models

- 🔍 Vector-based retrieval via FAISS for domain-relevant, context-aware search

- 🤖 LangChain-powered prompt pipelines for multi-turn, conversational LLM responses

- 🚀 Flask backend with REST endpoints for API integration and document processing

- 💬 Streamlit frontend with a lightweight chat interface

- ⚙️ Fully bootstrapped with Docker Compose for easy setup

Originally developed as a hands-on exploration of modern RAG pipelines, this project serves as a reference implementation for building domain-aware AI assistants and chatbots over private datasets.
