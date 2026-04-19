from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)
try:
    with open("key.txt", "rb") as f:
        key = f.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("key.txt", "wb") as f:
        f.write(key)

cipher = Fernet(key)


@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json or {}
    text = data.get("text", "")
    encrypted = cipher.encrypt(text.encode()).decode()
    return jsonify({"encrypted": encrypted})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json or {}
    text = data.get("text", "")
    decrypted = cipher.decrypt(text).decode()
    return jsonify({"decrypted": decrypted})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
