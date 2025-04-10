"""Module for document retrieval using a vector store."""

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever

from rag_app.utils.configs import RETRIEVER_CONFIGS


def get_retriever(vector_store: FAISS) -> VectorStoreRetriever:
    """Create a retriever from the given vector store."""
    return vector_store.as_retriever(
        search_type=RETRIEVER_CONFIGS["search_type"],
        search_kwargs=RETRIEVER_CONFIGS["search_kwargs"],
    )


def retrieve_documents(vector_store: FAISS, query: str) -> list[Document]:
    """Retrieve relevant documents from the vector store based on the query."""
    if not query:
        raise ValueError("Query cannot be empty!")
    retriever = get_retriever(vector_store)
    retrieved_documents = retriever.invoke(query)
    return retrieved_documents
