import allure
import pytest
import requests

def create_token():
    url="https://restful-booker.herokuapp.com/auth "
    headers={"Content-Type": "application/json"}
    payload={
    "username" : "admin",
    "password" : "password123"
    }
    response=requests.post(url=url,headers=headers,json=payload)
    token= response.json()["token"]
    print(token)
    return token

def create_booking():
    url="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type": "application/json"}
    payload={
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
    responseData= requests.post(url=url,headers=headers,json=payload)
    data=responseData.json()
    print(data)
    assert responseData.status_code == 200
    data=responseData.json()
    bookingid=data["bookingid"]
    return bookingid

def test_put_request():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking/" + str(create_booking())
    PUT_URL=base_url+base_path
    cookie= "token= "+ str(create_token())
    headers= {
        "Content-Type": "application/json",
        "cookie":cookie
    }
    payload={
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    assert response.status_code == 200
    print(response.json())
    assert response.json()["firstname"] == "James"


def test_delete_request():
    url="https://restful-booker.herokuapp.com/booking/"
    booking_id= create_booking()
    DELETE_URL=url+booking_id
    cookie_value="token=" + str(create_token())
    headers={
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)
    response=requests.delete(url=DELETE_URL,headers=headers)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "James"