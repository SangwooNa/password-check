import streamlit as st
from streamlit.web.server import server

# 비밀번호 설정
PASSWORD = "1234"

# Streamlit 앱 UI
st.title("Streamlit Login Server")
st.write("This server authenticates password requests.")

# 서버 설정
def configure_server():
    # Streamlit의 Tornado 웹 서버에 접근
    from tornado.web import RequestHandler
    from streamlit.web.server import server

    class LoginHandler(RequestHandler):
        def set_default_headers(self):
            self.set_header("Access-Control-Allow-Origin", "*")  # 모든 도메인 허용
            self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

        def options(self):
            self.set_status(204)
            self.finish()

        def post(self):
            import json
            try:
                # 요청 데이터 파싱
                data = json.loads(self.request.body)
                if data.get("password") == PASSWORD:
                    self.write(json.dumps({"success": True}))
                else:
                    self.write(json.dumps({"success": False}))
            except Exception as e:
                self.set_status(400)
                self.write(json.dumps({"error": str(e)}))

    # Tornado 서버에 핸들러 추가
    app = server.server._http_server._tornado_app
    app.add_handlers(".*$", [(r"/login", LoginHandler)])

# 서버 구성 실행
configure_server()

st.write("Send POST requests to the `/login` endpoint to authenticate.")
