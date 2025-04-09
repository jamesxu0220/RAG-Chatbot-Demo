"""Module to split documents into smaller chunks for processing."""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from rag_app.utils.configs import (
    CHUNK_OVERLAP_TOKENS,
    CHUNK_SIZE_TOKENS,
    EMBEDDING_MODEL_OPENAI,
)


def split_documents(documents: list[Document]) -> list[Document]:
    """Split documents into smaller chunks based on token size.

    Parameters
    ----------
    documents : list[Document]
        List of documents to be split.

    Returns
    -------
    list[Document]
        List of split documents.
    """
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name=EMBEDDING_MODEL_OPENAI,
        chunk_size=CHUNK_SIZE_TOKENS,
        chunk_overlap=CHUNK_OVERLAP_TOKENS,
    )
    return text_splitter.split_documents(documents)


if __name__ == "__main__":
    from rag_app.ingest.document_loader import get_file_paths, load_documents

    file_paths = get_file_paths()
    documents = load_documents(file_paths)
    print(len(documents))
    print([len(doc.page_content) for doc in documents])

    split_docs = split_documents(documents)
    print(len(split_docs))
    print([len(doc.page_content) for doc in split_docs])
