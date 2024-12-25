import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel():
    return "xyz"

@pytest.fixture()
def read_json():
    return {}

def test_consume(create_token,create_booking_id,read_excel,read_json):
    print(create_token)
    print(create_booking_id)
    print(read_excel)
    print(read_json)


