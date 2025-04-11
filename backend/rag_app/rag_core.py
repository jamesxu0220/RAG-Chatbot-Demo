"""RAG pipeline backend."""

from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough

from rag_app.rag.llm import get_llm
from rag_app.rag.prompts import get_default_prompt
from rag_app.rag.retrieval import get_retriever
from rag_app.vector_stores.vector_store import get_vector_store

_conversations: list[tuple[str, str]] = []


def get_conversation_history() -> list[tuple[str, str]]:
    """Get stored conversation history from Flask's g object."""
    global _conversations
    return _conversations


def record_conversation(messages: list[tuple[str, str]]) -> None:
    """Record the conversation messages."""
    global _conversations
    _conversations.extend(messages)


def get_rag_chain() -> Runnable:
    """Create and return the RAG chain for processing queries."""
    retriever = get_retriever(get_vector_store())
    inputs = {
        "context": retriever,
        "question": RunnablePassthrough(),
        "conversation": RunnableLambda(lambda _: get_conversation_history()),
    }
    prompt = get_default_prompt()
    llm = get_llm()

    chain = inputs | prompt | llm | StrOutputParser()
    return chain
