
import os

from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "groq/openai/gpt-oss-20b"

app = Flask(__name__)

PERSONAS = {
    "Friendly": (
        "You are MAST AI by Divya, a friendly and helpful assistant. "
        "Be conversational, engaging, and clear."
    ),
    "Teacher": (
        "You are an excellent teacher. Explain concepts step by step "
        "with simple examples."
    ),
    "Coder": (
        "You are an expert programming assistant. Provide correct code "
        "and explain the important logic."
    ),
    "Creative": (
        "You are a creative assistant who suggests original ideas "
        "and interesting solutions."
    ),
    "Professional": (
        "You are a professional assistant. Give clear, structured, "
        "and practical answers."
    ),
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    if not API_KEY:
        return jsonify({
            "error": "GROQ_API_KEY is not configured on the server."
        }), 500

    data = request.get_json(silent=True) or {}

    user_messages = data.get("messages", [])
    persona = data.get("persona", "Friendly")

    if persona not in PERSONAS:
        persona = "Friendly"

    if not isinstance(user_messages, list) or not user_messages:
        return jsonify({"error": "Please enter a message."}), 400

    # Keep only valid user/assistant messages and recent context.
    safe_messages = []

    for message in user_messages[-20:]:
        if not isinstance(message, dict):
            continue

        role = message.get("role")
        content = message.get("content")

        if role not in ("user", "assistant"):
            continue

        if not isinstance(content, str) or not content.strip():
            continue

        safe_messages.append({
            "role": role,
            "content": content[:12000]
        })

    if not safe_messages or safe_messages[-1]["role"] != "user":
        return jsonify({
            "error": "Your latest message must be a user message."
        }), 400

    try:
        response = completion(
            model=MODEL,
            api_key=API_KEY,
            messages=[
                {
                    "role": "system",
                    "content": PERSONAS[persona]
                }
            ] + safe_messages,
            temperature=0.7,
            max_tokens=1200
        )

        answer = response.choices[0].message.content or ""

        return jsonify({"reply": answer})

    except Exception:
        app.logger.exception("Groq request failed")

        return jsonify({
            "error": (
                "Sorry, I couldn't get a response. "
                "Check the server's API configuration, model access, "
                "internet connection, and API quota."
            )
        }), 502


if __name__ == "__main__":
    app.run(debug=False)
