from datastore.db import Database
import pytest


@pytest.fixture
def test_db_empty() -> Database:
    db = Database()
    return db

@pytest.fixture
def test_db_with_table(test_db_empty):
    test_db_empty.create_table()
    return test_db_empty

@pytest.fixture
def test_db(test_db_with_table):
    test_db_with_table.insert_into("192.168.100.1")
    return test_db_with_table


def test_create_table(test_db_empty):
    test_db_empty.create_table()


def test_insert_into(test_db_with_table):
    test_db_with_table.insert_into("192.168.100.1")
    # ...


@pytest.mark.parametrize("ip_address, expected",[
    ("localhost","10.0.0.2"),
    ("192.168.3.11",'192.168.3.11')
])
def test_list_servers(ip_address, expected, test_db):
    test_db.insert_into(ip_address)

    servers = test_db.list_servers()
    assert isinstance(servers, list)
    assert servers == expected


@pytest.mark.parametrize("ip", [
    pytest.param("192.168.1.1", id="default ip")
])
def test_delete_server(ip, test_db: Database):
    assert ip in test_db.list_servers()
    test_db.delete_server(ip)
    assert ip not in test_db.list_servers()

