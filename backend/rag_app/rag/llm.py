"""LLM units that serve the RAG."""

from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    """Initialize and return an LLM instance."""
    return ChatOpenAI(model="gpt-4o")
