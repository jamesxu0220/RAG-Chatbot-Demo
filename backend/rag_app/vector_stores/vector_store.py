"""Module to create embedding for documents and store them in a vector store."""

import os

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from rag_app.utils.api_key import get_openai_api_key
from rag_app.utils.configs import EMBEDDING_MODEL_OPENAI


def embed_and_store_documents(
    documents: list[Document], save_path: str = "faiss_index"
) -> FAISS:
    """Embed documents and store them in a FAISS vector store."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Loading OpenAI API key from environment variables...")
        get_openai_api_key()
        print("Loaded!")
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL_OPENAI)
    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local(save_path)
    return vectorstore


def load_vector_store(file_path: str = "faiss_index") -> FAISS:
    """Load the FAISS vector store from the specified path."""
    # Check if 'faiss_index' file exists in the current directory
    if not os.path.exists(f"{file_path}/index.faiss") or not os.path.exists(
        f"{file_path}/index.pkl"
    ):
        raise FileNotFoundError(
            f"Vector store {file_path} not found. "
            "Please embed and store documents first."
        )

    vectorstore = FAISS.load_local(
        file_path,
        OpenAIEmbeddings(model=EMBEDDING_MODEL_OPENAI),
        allow_dangerous_deserialization=True,
    )
    return vectorstore
