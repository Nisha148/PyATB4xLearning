import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 123

def test_1(create_token,create_booking_id):
    print("Token-> ",create_token)
    print("Booking_ID-> ",create_booking_id)


def test_2(create_token, create_booking_id):
    print("Token-> ", create_token)
    print("Booking_ID-> ", create_booking_id)

