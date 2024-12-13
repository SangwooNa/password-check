import streamlit as st
from tornado.web import RequestHandler
from streamlit.web.server import Server

# 비밀번호 설정
PASSWORD = "your_password"

# Tornado 핸들러 클래스 생성
class LoginHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 모든 도메인 허용
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

    def options(self):
        self.set_status(204)
        self.finish()

    def post(self):
        import json
        try:
            # JSON 요청 데이터 읽기
            data = json.loads(self.request.body)
            if data.get("password") == PASSWORD:
                self.write(json.dumps({"success": True}))
            else:
                self.write(json.dumps({"success": False}))
        except Exception as e:
            self.set_status(400)
            self.write(json.dumps({"error": str(e)}))

# Tornado 서버에 핸들러 추가
def add_cors_support():
    server = Server.get_current()
    app = server._http_server._tornado_server.application
    app.add_handlers(r".*", [(r"/login", LoginHandler)])

# Streamlit 앱
st.title("Streamlit Login with CORS")
st.write("Send POST requests to the `/login` endpoint to test password verification.")

# Tornado CORS 설정 추가
add_cors_support()
