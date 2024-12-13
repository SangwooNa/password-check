import streamlit as st

# 비밀번호 설정
PASSWORD = "your_password"

# 쿼리 파라미터 읽기
query_params = st.experimental_get_query_params()

# Streamlit 앱 페이지
st.title("Streamlit Login")
st.write("This app processes password verification using query parameters.")

if "password" in query_params:
    input_password = query_params.get("password", [None])[0]  # 쿼리에서 비밀번호 가져오기
    if input_password == PASSWORD:
        st.success("Login successful!")
    else:
        st.error("Login failed!")
else:
    st.write("Please send a password via query parameters to verify.")
