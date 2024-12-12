import streamlit as st
from flask import Flask, request, jsonify
from streamlit.web.server.websocket_headers import get_websocket_headers
from streamlit.web.server.websocket_route import add_websocket_route

# Flask 애플리케이션 생성
app = Flask(__name__)

# 비밀번호와 API 키 설정
VALID_PASSWORD = "1234"
API_KEY = "1703dff40703ad3b88e94cf037946d6d"

# Flask 경로 설정
@app.route("/validate", methods=["POST"])
def validate_password():
    try:
        data = request.json
        if data["password"] == VALID_PASSWORD:
            return jsonify({"success": True, "apiKey": API_KEY})
        else:
            return jsonify({"success": False, "message": "Invalid password"}), 401
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

# Streamlit에서 Flask 연동
def main():
    st.title("Streamlit 서버 실행 중")
    st.write("HTML 파일에서 비밀번호 검증 요청을 처리합니다.")

    # Flask 애플리케이션 실행
    from werkzeug.serving import make_server
    server = make_server("localhost", 8501, app)
    server.serve_forever()

if __name__ == "__main__":
    main()
