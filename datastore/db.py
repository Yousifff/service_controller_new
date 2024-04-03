import sqlite3
from datetime import datetime,date
import pathlib

DATASTORE_PATH = pathlib.Path(__file__).parent.absolute()
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATASTORE_PATH / 'service_controller.db',check_same_thread=False)
        self.cursor = self.conn.cursor()

    '''def create_table(self):
        table = """ CREATE TABLE  IF NOT EXISTS servers (
            ip TEXT NOT NULL,
            date timestamp
        ); """
        self.cursor.execute(table)
    '''
    def insert_into(self,ip,service):
        self.cursor.execute("INSERT INTO servers VALUES (?,?);", (ip, service))
        self.conn.commit()

    def list_servers(self):
        servers = self.cursor.execute("SELECT ip FROM servers;")
        servers_list = []
        for server in servers:
            servers_list.append(server[0])

        return servers_list

    def delete_server(self, server_ip):
        sql_comm = f"DELETE FROM servers WHERE ip=?;"
        self.cursor.execute(sql_comm, (server_ip,))
        self.conn.commit()
    
    
    
    def list_services(self):
        services = self.cursor.execute("SELECT service from servers;").fetchall()
        svc_list = []
        for serv in services:
            svc_list.append(serv[0])
        return svc_list
    
    def add_username(self,username,password):
        self.cursor.execute("INSERT INTO users VALUES (?,?);",(username,password))
        self.conn.commit()
        
    def list_users(self):
        users = self.cursor.execute("SELECT * FROM users;")
        return users
    
    def user_login(self,username,password):
        result = self.cursor.execute('SELECT * FROM users WHERE usernme=? AND password=?;',(username,password))
        self.conn.commit()
        return result.fetchone()
    
    def add_privilege(self,ip,username,permission):
        self.cursor.execute(f"INSERT INTO permissions  VALUES (?,?,?)",(ip,username,permission))    
        self.conn.commit()
        
    def get_user_permission(self,username):
        stat = self.cursor.execute(f"SELECT button_name from permissions WHERE username=?;",(username,)).fetchall()
        status_list = [svc[0] for svc in stat]
        
        return status_list