"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, current_app, jsonify
from langchain_community.vectorstores import FAISS

base = Blueprint("base", __name__)
rag = Blueprint("rag", __name__)


@base.route("/", methods=["GET"])
@base.route("/status", methods=["GET"])
def status():
    """Return the status of the application."""
    return jsonify({"status": "NORMAL"}), 200


@rag.route("/vectorstore-ready", methods=["GET"])
def vectorstore_ready():
    """Check if the vector store is loaded and ready."""
    vector_store = current_app.config.get("VECTORSTORE")
    ready = isinstance(vector_store, FAISS)
    return jsonify({"vectorstore_loaded": ready}), 200
