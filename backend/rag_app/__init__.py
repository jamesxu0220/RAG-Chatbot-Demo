"""Inits the Flask app."""

from flask import Flask

from rag_app.routes import base, rag
from rag_app.vector_stores.vector_store import get_vector_store


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(base)
    app.register_blueprint(rag, url_prefix="/rag")

    get_vector_store()  # Ensure vector store is loaded at startup
    return app
