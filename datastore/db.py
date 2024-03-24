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
        rows = self.cursor.execute("SELECT ip FROM servers;")
        return rows.fetchall()

    def delete_server(self, server_ip):
        sql_comm = f"DELETE FROM servers WHERE ip=?;"
        self.cursor.execute(sql_comm, (server_ip,))
        self.conn.commit()
    
    
    
    def list_services(self):
        services = self.cursor.execute("SELECT service from servers;").fetchall()
        return services
    
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
    
    def add_privilege(self,ip,username,stop,start):
        if stop:
            self.cursor.execute("INSERT INTO permissions VALUES (?,?,?,?,?)",(ip,username,1,0,0))
        else:
            self.cursor.execute("INSERT INTO permissions VALUES (?,?,?,?,?)",(ip,username,0,0,1))
        self.conn.commit()