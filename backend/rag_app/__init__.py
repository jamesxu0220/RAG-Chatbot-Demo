"""Inits the Flask app."""

from flask import Flask

from rag_app.ingestion import document_ingestion
from rag_app.routes import base, rag
from rag_app.vector_stores.vector_store import load_vector_store


def create_app() -> Flask:
    app = Flask(__name__)

    try:
        vector_store = load_vector_store()
    except FileNotFoundError:
        vector_store = document_ingestion()
    app.config["VECTORSTORE"] = vector_store

    app.register_blueprint(base)
    app.register_blueprint(rag, url_prefix="/rag")
    return app
