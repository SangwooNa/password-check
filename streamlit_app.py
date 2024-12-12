from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # CORS 활성화

@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.json
    if data.get('password') == '1234':  # 비밀번호 설정
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Invalid password"})

@app.route('/fetch-book-info', methods=['POST'])
def fetch_book_info():
    data = request.json
    book_name = data.get('bookName', '')
    KAKAO_API_KEY = "YOUR_KAKAO_API_KEY"  # 카카오 API 키
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    url = f"https://dapi.kakao.com/v3/search/book?target=title&query={book_name}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['documents']:
            book = data['documents'][0]
            return jsonify({"title": book['title'], "author": ", ".join(book['authors'])})
    return jsonify({"title": "N/A", "author": "N/A"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
