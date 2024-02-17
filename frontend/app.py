import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def create_form():
    st.markdown("<h1 style='text-align:center;'>login page</h1>", unsafe_allow_html=True)
    with st.form("Login"):
        username = st.text_input("username")
        password = st.text_input("password", type="password")
        submit_button = st.form_submit_button("Click")
        if submit_button:
            if username and password:

                st.success("Logged in successfully")
                st.switch_page("pages/servers.py")
            else:
                st.warning("Invalidd username or password")

create_form()