"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, jsonify

from rag_app.ingestion import document_ingestion
from rag_app.vector_stores.vector_store import load_vector_store

base = Blueprint("base", __name__)
rag = Blueprint("rag", __name__)


@base.route("/", methods=["GET"])
@base.route("/status", methods=["GET"])
def status():
    """Return the status of the application."""
    return jsonify({"status": "NORMAL"}), 200


@rag.route("/load-docs", methods=["POST"])
def load_documents():
    """Load documents into a vector store and save the index to local directory."""
    document_ingestion()
    return jsonify({"status": "Documents loaded successfully"}), 200


@rag.route("/check-vector_store", methods=["GET"])
def get_vector_store():
    """Check whether the vector store had been created."""
    try:
        load_vector_store()
        return jsonify({"status": "Vector store loaded successfully"}), 200
    except FileNotFoundError:
        return (
            jsonify({"status": "Vector store not found. Please load documents first."}),
            404,
        )
