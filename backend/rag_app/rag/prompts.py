"""Prompts for the property management assistant application."""

from langchain_core.prompts import ChatPromptTemplate

SYSTEM_INSTRUCTION = (
    "system",
    """
    You are a helpful assistant to the user dealing with property management related
    questions. Use the context provided to answer the question.
    If the context offers related details (e.g., location, amenities, or challenges),
    you may make broad or general recommendations based on those.
    Even if not explicitly stated, if specific properties are mentioned
    in the context, you should highlight them with a brief explanation of what makes
    them notable based on the information provided (e.g., location, amenities, or
    appeal). You may confidently recommend one or more properties as suitable options
    as long as the information comes from context. Do not make up any facts not
    present in the context.
    """,
)

CHAT_HISTORY = ("placeholder", "{conversation}")

USER_QUERY_MESSAGE = (
    "human",
    """
    Context:
    {context}

    Question:
    {question}

    Answer:
    """,
)


def get_default_prompt() -> ChatPromptTemplate:
    """Get the default prompt template."""
    prompt_messages = [SYSTEM_INSTRUCTION, CHAT_HISTORY, USER_QUERY_MESSAGE]
    return ChatPromptTemplate(prompt_messages)
