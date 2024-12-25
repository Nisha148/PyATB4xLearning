import requests
import pytest


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "passwdord123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    Data = response.text
    print(Data)
    return token

@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/"
    URL = base_url + path
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
    responseData = requests.post(url=URL, headers=headers, json=payload)
    data = responseData.json()
    print(data)
    bookingid = data["bookingid"]
    return bookingid

@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"

@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "closed"