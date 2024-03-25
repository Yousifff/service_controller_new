
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datastore.db import Database

db = Database()

if 'username' not in st.session_state:
    st.session_state['username'] = None
    st.session_state['role'] = None

def create_form():
    st.markdown("<h1 style='text-align:center;'>login page</h1>", unsafe_allow_html=True)
    with st.form("Login"):
        username = st.text_input("username").lstrip()
        password = st.text_input("password", type="password").lstrip()
        submit_button = st.form_submit_button("Click")
        if submit_button:
            if db.user_login(username,password):
                st.session_state['username'] = username
                st.session_state['role'] = 'user'
                st.success("Logged in successfully")
                st.switch_page("frontend/pages/admin_v2.py")
                    
            else:
                st.warning("Invalidd username or password")