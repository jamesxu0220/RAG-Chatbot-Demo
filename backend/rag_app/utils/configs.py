"""Various tuneable configs for the RAG app."""

CHUNK_SIZE_TOKENS = 300
CHUNK_OVERLAP_TOKENS = 50
EMBEDDING_MODEL_OPENAI = "text-embedding-3-small"
RETRIEVER_CONFIGS = {
    "search_type": "similarity_score_threshold",
    "search_kwargs": {
        "score_threshold": 0.15,
        "k": 5,
    },
}
