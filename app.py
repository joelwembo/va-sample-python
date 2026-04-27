"""Minimal Flask sample app used as a Valtunox deployment target."""
import os
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

INDEX_HTML = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")


@app.get("/")
def root():
    return INDEX_HTML


@app.get("/health")
def health():
    return jsonify(message="If you see this, your app is running well!")


if __name__ == "__main__":
    port = int(os.environ.get("app_port", 8000))
    app.run(host="0.0.0.0", port=port)
