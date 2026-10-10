
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "message": "AI Agent Team Backend is running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Please provide a message"}), 400

    if not client:
        return jsonify({
            "error": "GEMINI_API_KEY is not configured"
        }), 503

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return jsonify({
            "reply": response.text or "No response received"
        })
    except Exception:
        app.logger.exception("Gemini request failed")
        return jsonify({
            "error": "AI request failed. Check server logs and API settings."
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
