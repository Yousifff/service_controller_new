import streamlit as st

if 'server_list' and 'user_list' not in st.session_state:
    st.session_state['server_list'] = []
    st.session_state['user_list'] = []



def managment():
    type_of_administration = st.selectbox("Managment Option",['server','user'],key="type")
    if type_of_administration == 'server':
        add = st.radio("Managing Server", ['Add', 'List', 'Remove'], label_visibility="collapsed", key='m_server')
        # list_servers = st.checkbox("List Servers",key=2)
        # remove = st.checkbox("Remove Server",key=3)
        if add == 'Add':
            server_ip = st.text_input("Server IP Address").strip()
            st.session_state['server_list'].append(server_ip.strip())

        if add == 'List':
            servers = [server.strip() for server in st.session_state['server_list'] if server != ""]
            st.table(servers)
        if add == 'Remove':
            server_ip = st.text_input("Server IP Address")
            st.session_state['server_list'].remove(server_ip)

    elif type_of_administration == 'user':
        add = st.radio("Managing User", ['Add', 'List', 'Remove'])
        if add == 'Add':
            username = st.text_input("username").strip()
            st.session_state['user_list'].append(username.strip())

        if add == 'List':
            users = [user.strip() for user in st.session_state['user_list'] if user != ""]
            st.table(users)
        if add == 'Remove':
            username = st.text_input("Username")
            st.session_state['user_list'].remove(username)

managment()








