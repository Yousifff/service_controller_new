from datastore.db import Database
import pytest


@pytest.fixture
def test_db():
    db = Database()
    db.create_table()
    # db.insert_into("192.168.100.1")
    return db


@pytest.mark.parametrize("ip_address, expected",[
    ("10.0.0.2","10.0.0.2"),
    ("192.168.3.11",'192.168.3.11')
])
def test_list_servers(ip_address, expected, test_db):
    test_db.insert_into(ip_address)

    servers = test_db.list_servers()
    assert isinstance(servers, list)
    assert servers[0] == expected


@pytest.mark.parametrize("ip, expected", [
    ("192.168.1.1", "")
])
def test_delete_server(ip, expected, test_db):
    test_db.delete_server(ip)
    assert ip not in test_db.list_servers()
