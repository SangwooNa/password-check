from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 비밀번호와 Kakao API 키 설정
PASSWORD = "1357"
KAKAO_API_KEY = "1703dff40703ad3b88e94cf037946d6d"
ISBN_API_KEY = "4cf84b2d25cec9fff52f27a3d18bdc6124fc6a4aa3c257ad2e969a1f1558469b"

# 비밀번호 검증 엔드포인트
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    input_password = data.get("password")

    if input_password == PASSWORD:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid password!"}), 401

# API 키 제공 엔드포인트
@app.route("/get-api-key", methods=["GET"])
def get_api_key():
    return jsonify({"apiKey": ISBN_API_KEY})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
