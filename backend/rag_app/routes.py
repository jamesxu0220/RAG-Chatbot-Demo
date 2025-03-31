"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, jsonify

base = Blueprint("base", __name__)


@base.route("/status", methods=["GET"])
def status():
    """Return the status of the application."""
    return jsonify({"status": "NORMAL"}), 200
