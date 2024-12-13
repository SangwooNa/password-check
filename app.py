from flask import Flask, request, jsonify

app = Flask(__name__)

PASSWORD = "your_password"  # 원하는 비밀번호 설정

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()  # 클라이언트 요청에서 JSON 데이터를 받음
    input_password = data.get("password")
    if input_password == PASSWORD:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid password!"})

@app.route("/")
def home():
    return "Flask app is running!"  # 기본 라우트로 앱 상태 확인 가능

if __name__ == "__main__":
    app.run(debug=True)
