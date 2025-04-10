"""Inits the Flask app."""

from flask import Flask

from rag_app.routes import base, rag


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(base)
    app.register_blueprint(rag, url_prefix="/rag")
    return app
