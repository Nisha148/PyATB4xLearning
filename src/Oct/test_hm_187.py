import allure
import pytest
import requests

class Test_put_patch_request():
    def test_put_request(self,create_token,create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/" + str(create_booking())
        PUT_URL = base_url + base_path
        cookie = "token= " + str(create_token())
        headers = {
            "Content-Type": "application/json",
            "cookie": cookie
        }
        payload = {
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
        data = response.json()
        print(data)
        assert data["firstname"] == "James"