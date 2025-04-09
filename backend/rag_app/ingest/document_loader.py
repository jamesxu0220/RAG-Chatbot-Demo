"""Document loader for ingesting text files into the application."""

import os

from langchain_community.document_loaders.text import TextLoader
from langchain_core.documents import Document


def get_file_paths() -> list[str]:
    """Get the paths of all text files in the docs directory.

    Returns
    -------
    list[str]
        A list of file paths.
    """
    module_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(module_dir, "../docs")
    return [os.path.join(docs_dir, file) for file in os.listdir(docs_dir)]


def load_documents(file_paths: list[str]) -> list[Document]:
    """Load documents from the given file paths.

    Parameters
    ----------
    file_paths : list[str]
        A list of file paths to load.

    Returns
    -------
    list[Document]
        A list of loaded documents.
    """
    documents = []
    for file_path in file_paths:
        loader = TextLoader(file_path, encoding="utf-8")
        loaded_docs = loader.load()
        documents.extend(loaded_docs)
    return documents


if __name__ == "__main__":
    file_paths = get_file_paths()
    documents = load_documents(file_paths)
    print(documents[0].page_content)
