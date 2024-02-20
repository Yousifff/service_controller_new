import streamlit as st
import pandas as pd



def servers_list():
    servers = [f'192.168.100.{str(i)}' for i in range(10)]
    st.table(servers)



servers_list()



