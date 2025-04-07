"""Utility to get API key."""

import os

from dotenv import load_dotenv


def get_openai_api_key() -> str:
    """Load the OpenAI API key from the environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return api_key
