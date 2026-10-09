
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "project": "AI Agent Team",
        "message": "AI Agent backend is running"
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is required"}), 400

    if not client:
        return jsonify({
            "error": "GEMINI_API_KEY is not configured"
        }), 500

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return jsonify({
            "reply": response.text or "কোনো উত্তর পাওয়া যায়নি।"
        })
    except Exception:
        app.logger.exception("Gemini request failed")
        return jsonify({
            "error": "AI response failed. Check server logs."
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "10000"))
    )
