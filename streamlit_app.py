import streamlit as st
from flask import Flask, request, jsonify
from threading import Thread

# Flask 앱 생성
app = Flask(__name__)

# 비밀번호 설정
PASSWORD = "your_password"  # 비밀번호는 여기에서 설정

@app.route('/login', methods=['POST'])
def login():
    # 요청에서 비밀번호 추출
    data = request.json
    input_password = data.get("password")
    # 비밀번호 검증
    if input_password == PASSWORD:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# Streamlit에서 Flask 서버 실행
def run_flask():
    app.run(host='0.0.0.0', port=8500)

# Streamlit 앱 시작
if __name__ == '__main__':
    st.title("Streamlit Login Server")
    st.write("This server is for password verification only.")
    # Flask 서버를 별도 스레드에서 실행
    thread = Thread(target=run_flask)
    thread.daemon = True
    thread.start()
    st.write("Flask server running on port 8500.")
