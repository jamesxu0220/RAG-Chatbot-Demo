"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, jsonify
from langchain_community.vectorstores import FAISS

from rag_app.vector_stores.vector_store import get_vector_store

base = Blueprint("base", __name__)
rag = Blueprint("rag", __name__)


@base.route("/", methods=["GET"])
@base.route("/status", methods=["GET"])
def status():
    """Return the status of the application."""
    return jsonify({"status": "NORMAL"}), 200


@rag.route("/ping-vector-store", methods=["GET"])
def check_vector_store_ready():
    """Check if the vector store is loaded and ready."""
    vector_store = get_vector_store()
    ready = isinstance(vector_store, FAISS)
    return jsonify({"vector_store_loaded": ready}), 200
