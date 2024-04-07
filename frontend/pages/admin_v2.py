import streamlit as st
import extra_streamlit_components as stx

from datastore.db import Database
import paramiko
from paramiko import SSHClient

import logging


db = Database()


def check_permissions_based_on_role(status, role):
    role_has_permissions = status in ["start", "stop"] and role in ["admin", "super-admin"]

    return role_has_permissions


def check_permissions_based_on_user(status):
    permission = db.get_user_permission(st.session_state['username'])
    
    # TODO: get value from database table
    #if permission[0][2] == 'full':
    #    return ['start','stop']
    #else:
    #    return [permission[0][2]]
    if status in permission:
        return True
    return False
db = Database()



server, user, privileges = st.tabs(["Server Managment", "User Managment",'Privileges'])



def create_dynamic_buttons(idx,status):
     for item in range(len(servers)):
         count = idx*len(servers) + item

         role_has_permissions = check_permissions_based_on_user(status)
         if role_has_permissions:

            action_button = st.button(status, key=count)

            
            if action_button:
                
                clinet = SSHClient()
                clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                clinet.connect(hostname="",username='',password='')
                command_string = f'sudo -S systemctl {status} {st.session_state["service"]}'

                logging.info("Attempting to execute the following command:")
                logging.info(command_string)
                
                stdin,stdout,stderr = clinet.exec_command(command=command_string)
                stdin.write("" + "\n")
                stdin.flush()
                print(f'STDOUT: {stdout.read().decode("utf8")}')
                print(f'STDERR: {stderr.read().decode("utf8")}') 
                clinet.close()

         else:
            continue
def generate_services(idx,services):
    for service in range(len(services)):
        count = idx*len(services) + service
        st.text(services[service])
       

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
        
        col1, col2, col3, col4 = st.columns(4)

        #role = st.session_state["role"]
        with col1:
            servers = db.list_servers()
            for server in servers:
                st.markdown(server)
        with col2:
            create_dynamic_buttons(100,'stop')
        #with col3:
        #    create_dynamic_buttons(200,'restart')
        with col3:
            create_dynamic_buttons(300,'start')

        with col4:
            services = db.list_services()
            generate_services(400,services)
                
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
        server_ip = st.text_input("Server IP").lstrip()
        username = st.text_input("username").lstrip()
        btn_name = st.text_input("button name").lstrip()
        
        submit = st.form_submit_button("Save")
        if submit:
            db.add_privilege(server_ip,username,btn_name)
            