import streamlit as st
from datastore.db import Database



def managing_server(u_key=1):
    add = st.radio("Managing Server", ['Add', 'List', 'Remove'], label_visibility="collapsed", key=u_key)
    # list_servers = st.checkbox("List Servers",key=2)
    # remove = st.checkbox("Remove Server",key=3)
    if add == 'Add':
        server_ip = st.text_input(label="IP").strip()
        server_ip = server_ip.lstrip("")
        db = Database()
        db.create_table()
        db.insert_into(server_ip)

    if add == 'List':
        db = Database()
        servers = db.list_servers()
        st.table(servers)
    if add == 'Remove':
        server_ip = st.text_input("Server IP Address")
        st.session_state['server_list'].remove(server_ip)

def managing_user(u_key=2):
    add = st.radio("Managing User", ['Add', 'List', 'Remove'],key=u_key)
    if add == 'Add':
        username = st.text_input("username").strip()
        st.session_state['user_list'].append(username.strip())

    if add == 'List':
        users = [user.strip() for user in st.session_state['user_list'] if user != ""]
        st.table(users)
    if add == 'Remove':
        username = st.text_input("Username")
        st.session_state['user_list'].remove(username)


def managment():
    type_of_administration = st.selectbox("Managment Option",['server','user'],key="type")
    if type_of_administration == 'server':
        managing_server()

    elif type_of_administration == 'user':
        managing_user()

managment()








