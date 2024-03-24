import streamlit as st
import extra_streamlit_components as stx

from datastore.db import Database
import paramiko
from paramiko import SSHClient






db = Database()

server, user, privileges = st.tabs(["Server Managment", "User Managment",'Privileges'])



def create_dynamic_buttons(idx,status):
    
     for item in range(len(servers)):
         count = idx*len(servers) + item
         action_button = st.button(status, key=count)
         
         if action_button:
             
             clinet = SSHClient()
             clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
             
             clinet.connect(hostname="192.168.100.114",username='yousif',password='Ss@s1598')
             stdin,stdout,stderr = clinet.exec_command(f'sudo -S systemctl {status} {st.session_state["service"]}')
             stdin.write("Ss@s1598" + "\n")
             stdin.flush()
             print(f'STDOUT: {stdout.read().decode("utf8")}')
             print(f'STDERR: {stderr.read().decode("utf8")}') 
             clinet.close()

def generate_services(idx,service_name):
    for server in range(len(servers)):
        count = idx*len(servers) + server
        st.text(service_name)
        st.session_state['service'] = service_name
       

with server:
    adding_server, listing_servers, deleting_server = st.tabs(['Add', 'List', 'Delete'])
    with adding_server:

        with st.form("adding_server"):
            server_ip = st.text_input("Server IP").lstrip()
            service = st.text_input("service_name").lstrip()
            submit = st.form_submit_button("Save")
            if submit:
                db.insert_into(server_ip,service)
    with listing_servers:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            servers = db.list_servers()
            for server in servers:
                st.markdown(server[0])
        with col2:
            create_dynamic_buttons(100,'stop')
        with col3:
            create_dynamic_buttons(200,'restart')
        with col4:
            create_dynamic_buttons(300,'start')

        with col5:
            services = db.list_services()
            for service in services:
                service = service[0]
                generate_services(400,service)
                
    with deleting_server:
        with st.form("Delete Server"):
            server_ip = st.text_input("Server IP").lstrip()
            submit = st.form_submit_button("Delete")
            if submit:
                db.delete_server(server_ip)
                
                
with user:
    add_user, list_users , delete_user = st.tabs(['Add','List','Delete'])
    with add_user:
        with st.form("adding_users"):
            username = st.text_input("username").lstrip()
            password = st.text_input("Password",type="password").lstrip()
            submit = st.form_submit_button("Save")
            if submit:
                db.add_username(username,password)
    
    with list_users:
        users = db.list_users()
        st.table(users)
            

with privileges:
    with st.form("privileges"):
        stop_svc = False
        start_svc = False
        server_ip = st.text_input("Server IP").lstrip()
        username = st.text_input("username").lstrip()
        stop = st.checkbox('stop')
        start = st.checkbox("start")
        if stop:
            stop_svc = True
        
        if start:
            start_svc = True
        submit = st.form_submit_button("submit")
        if submit:
            db.add_privilege(server_ip,username,stop_svc,start_svc)