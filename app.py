from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 비밀번호와 Kakao API 키 설정
PASSWORD = "your_password"
KAKAO_API_KEY = "your_kakao_api_key_here"

# 비밀번호 검증 엔드포인트
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    input_password = data.get("password")

    if input_password == PASSWORD:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid password!"})

# API 키 제공 엔드포인트
@app.route("/get-api-key", methods=["GET"])
def get_api_key():
    # API 키 반환
    return jsonify({"apiKey": KAKAO_API_KEY})

if __name__ == "__main__":
    app.run(debug=True)
