from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 출처(origin) 허용

PASSWORD = "your_password"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("password") == PASSWORD:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid password!"})

@app.route("/")
def home():
    return "Flask app is running!"

if __name__ == "__main__":
    app.run(debug=True)
