"""Defines different blueprints (with corresponding routes as HTTP endpoints)."""

from flask import Blueprint, jsonify

base = Blueprint("", __name__)


@base.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "NORMAL"}), 200
