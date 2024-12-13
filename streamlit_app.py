import streamlit as st

# Streamlit 앱 설정
st.title("Streamlit Login Server")

# 비밀번호 설정
PASSWORD = "your_password"

# 클라이언트에서 요청 처리
with st.form("login_form"):
    st.write("Enter your password:")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Submit")

# 로그인 확인
if submit:
    if password == PASSWORD:
        st.success("Login successful!")
    else:
        st.error("Login failed!")

# HTML 설명
st.write("Use the HTML file to log in.")
