from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    user_ip = request.access_route[0]
    return render_template("generate.html", ip=user_ip)

@app.route("/generate", methods=["GET"])
def generate():
    key = Fernet.generate_key()
    return key

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json or {}
    text = data.get("text", "")
    key = data.get("key", "")
    cipher = Fernet(key)
    encrypted = cipher.encrypt(text.encode()).decode()
    return jsonify({"encrypted": encrypted})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json or {}
    text = data.get("text", "")
    key = data.get("key", "")
    cipher = Fernet(key)
    decrypted = cipher.decrypt(text).decode()
    return jsonify({"decrypted": decrypted})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
