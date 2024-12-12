import streamlit as st
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from threading import Thread

# Flask 앱 생성
app = Flask(__name__)
CORS(app)  # CORS 활성화

# 비밀번호 확인 API
@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.json
    password = data.get('password', '')
    if password == '1234':  # 비밀번호 설정
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Invalid password"})

# 카카오 API 호출 API
@app.route('/fetch-book-info', methods=['POST'])
def fetch_book_info():
    data = request.json
    book_name = data.get('bookName', '')

    if not book_name:
        return jsonify({"title": "N/A", "author": "N/A"})

    # 카카오 API 호출
    KAKAO_API_KEY = "YOUR_KAKAO_API_KEY"  # 카카오 API 키 입력
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    url = f"https://dapi.kakao.com/v3/search/book?target=title&query={book_name}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['documents']:
            book = data['documents'][0]
            return jsonify({"title": book['title'], "author": book['authors'][0]})
    return jsonify({"title": "N/A", "author": "N/A"})

# Flask 서버 시작 함수
def start_flask():
    app.run(host="0.0.0.0", port=8501)

# Streamlit 인터페이스
def main():
    st.title("Streamlit + Flask 통합 서버")
    st.write("HTML 파일과 통신하기 위한 서버가 실행 중입니다.")

# Flask 서버를 백그라운드에서 실행
Thread(target=start_flask).start()

if __name__ == '__main__':
    main()
