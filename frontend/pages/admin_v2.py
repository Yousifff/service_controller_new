import streamlit as st
import extra_streamlit_components as stx

from datastore.db import Database
db = Database()
db.create_table()
server, user = st.tabs(["Server Managment", "User Managment"])

with server:
    adding_server, listing_servers , deleting_server = st.tabs(['Add','List','Delete'])
    with adding_server:
        
        
        with st.form("adding_server"):
            server_ip = st.text_input("Server IP").lstrip()
            submit = st.form_submit_button("Save")
            if submit:
                db.insert_into(server_ip)        
    with listing_servers:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            servers = db.list_servers()
            for server in servers:
                st.markdown(server[0])
        with col2:
            for item in range(len(servers)):
                st.button("stop",key=item)

        with col3:
            idx = 1
            for item in range(len(servers)):
                st.button("restart",key=idx+5)
                idx += 1
        with col4:
            idx = 2
            for item in range(len(servers)):
                st.button("start",key=idx+10)
                idx += 1
        with col5:
            idx = 3
            for item in range(len(servers)):
                st.button("httpd",key=idx+20)
                idx += 1
    with deleting_server:
        with st.form("Delete Server"):
            server_ip = st.text_input("Server IP").lstrip()
            submit = st.form_submit_button("Delete")
            if submit:
                db.delete_server(server_ip)

            


