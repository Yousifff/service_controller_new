from datastore.db import Database
import pytest


@pytest.fixture
def test_db():
    db = Database()
    db.create_table()
    #db.insert_into("192.168.100.1")
    return db


@pytest.mark.parametrize("ip_address, expected",[
    ("localhost",'100.100.100.100'),
    ("192.168.3.11",'192.168.3.11')
])
def test_list_servers(ip_address,expected,test_db):
    test_db.insert_into(ip_address)

    servers = test_db.list_servers()
    assert isinstance(servers,list)
    assert servers == expected



