from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/api/message", methods=["GET"])
def message():
    return jsonify(message="Hello from backend service"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)