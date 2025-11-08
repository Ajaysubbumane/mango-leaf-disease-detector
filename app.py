"""Mango Leaf Disease Detector - Minimal Flask API"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Home endpoint"""
    return jsonify({
        "status": "OK",
        "project": "🌿 Mango Leaf Disease Detector",
        "version": "1.0",
        "message": "API is working!",
        "endpoints": {
            "GET /": "This page",
            "GET /health": "Health check"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({"status": "healthy", "ready": True}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
