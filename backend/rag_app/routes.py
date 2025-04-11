"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, jsonify, request
from langchain_community.vectorstores import FAISS

from rag_app.rag_core import (
    get_conversation_history,
    get_rag_chain,
    record_conversation,
)
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


@rag.route("/chat", methods=["POST"])
def chat():
    """Handle chat requests with RAG."""
    user_query = request.json.get("query").strip()
    if not isinstance(user_query, str) or not user_query:
        return jsonify({"error": "Query is required"}), 400
    try:
        chain = get_rag_chain()
        response = chain.invoke(user_query)
        record_conversation(
            [
                ("human", user_query),
                ("ai", response),
            ]
        )
    except Exception as e:
        return jsonify({"Unexpected error": str(e)}), 500
    return jsonify({"response": response}), 200


@rag.route("/chat-history", methods=["GET"])
def get_chat_history():
    """Get the conversation history."""
    history = get_conversation_history()
    return jsonify({"chat_history": history}), 200
