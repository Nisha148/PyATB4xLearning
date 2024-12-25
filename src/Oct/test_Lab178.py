import pytest
import requests
import allure
@allure.title("TC#1 - Verify the creation of a booking with valid data")
@allure.description("Create a booking and verify the response with valid data.")
@pytest.mark.crud
def test_create_booking_valid():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    booking = response_data["booking"]
    assert "bookingid" in response_data
    assert response_data["bookingid"] > 0
    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] is True
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"

@allure.title("TC#2 - Verify booking creation with an empty payload")
@allure.description("Attempt to create a booking with an empty payload and verify the failure response.")
@pytest.mark.crud
def test_create_booking_negative_empty_payload():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 500

@allure.title("TC#3 - Verify booking creation with negative price")
@allure.description("Create a booking with a negative total price and verify the response.")
@pytest.mark.crud
def test_create_booking_negative_price():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": -111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    booking = response_data["booking"]
    assert "bookingid" in response_data
    assert response_data["bookingid"] > 0
    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == -111
    assert booking["depositpaid"] is True
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"