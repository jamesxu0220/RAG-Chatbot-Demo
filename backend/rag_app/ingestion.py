"""Module to handle documents ingestion for the RAG application."""

from langchain_community.vectorstores import FAISS

from rag_app.ingest.chunking import split_documents
from rag_app.ingest.document_loader import get_file_paths, load_documents
from rag_app.vector_stores.vector_store import embed_and_store_documents


def document_ingestion() -> FAISS:
    """Ingest documents for the RAG application."""
    file_paths = get_file_paths()
    documents = load_documents(file_paths)
    split_docs = split_documents(documents)
    vector_store = embed_and_store_documents(split_docs)
    return vector_store


if __name__ == "__main__":
    document_ingestion()
