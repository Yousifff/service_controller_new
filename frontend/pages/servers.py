import streamlit as st


def servers_list():
    servers = [f'192.168.100.{str(i)}' for i in range(10)]
    st.table(servers)



servers_list()



