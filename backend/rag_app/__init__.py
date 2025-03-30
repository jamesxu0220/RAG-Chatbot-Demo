"""Inits the Flask app."""

from flask import Flask

from rag_app.routes import base


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(base)
    return app
