import streamlit as st

if 'server_list' not in st.session_state:
    st.session_state['server_list'] = []

def server_managment():
    add = st.radio("Managing Server",['Add','List','Remove'])
    #list_servers = st.checkbox("List Servers",key=2)
    #remove = st.checkbox("Remove Server",key=3)

    if add == 'Add':
        server_ip = st.text_input("Server IP Address").strip()
        st.session_state['server_list'].append(server_ip.strip())

    if add == 'List':
        servers = [server.strip() for server in st.session_state['server_list'] if server != ""]
        st.table(servers)
    if add == 'Remove':
        server_ip = st.text_input("Server IP Address")
        st.session_state['server_list'].remove(server_ip)








server_managment()
