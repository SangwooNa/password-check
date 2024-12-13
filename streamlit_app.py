import streamlit as st

# 비밀번호 설정
PASSWORD = "1234"

# Streamlit 앱
st.title("Password Verification Server")

# 쿼리 파라미터에서 비밀번호 요청 처리
query_params = st.experimental_get_query_params()

if "password" in query_params:
    # 클라이언트가 비밀번호를 보낸 경우 처리
    input_password = query_params.get("password")[0]  # 첫 번째 값 가져오기
    if input_password == PASSWORD:
        st.success("Login successful!")
    else:
        st.error("Login failed!")
else:
    st.write("Send a `password` parameter via query to verify.")

# 추가로 HTML 페이지에 URL 제공
st.write("Use `https://your-streamlit-app-url?password=your_password` to test.")
