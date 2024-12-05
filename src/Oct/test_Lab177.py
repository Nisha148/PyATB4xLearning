import pytest
import allure
import requests

@allure.title("TC#1 GET Request")
@allure.description("Verify the test case with booking id")
@allure.tag("regression","po","smoke")
@allure.label("owner","Nisanjini")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url= "https://restful-booker.herokuapp.com/booking/1"
    responseData= requests.get(url)
    print(responseData.text)
    print(responseData.json())
    print(responseData.headers)
    assert responseData.status_code==200

@allure.title("TC#2 GET Request")
@allure.description("Verify the test case with booking id with -1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url= "https://restful-booker.herokuapp.com/booking/-1"
    responseData= requests.get(url)
    assert responseData.status_code != 404

@allure.title("TC#3 GET Request")
@allure.description("Verify the test case with booking id with invalid")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url= "https://restful-booker.herokuapp.com/booking/invalid"
    responseData= requests.get(url)
    assert responseData.status_code == 404

@allure.title("TC#4 GET Request")
@allure.description("Verify the test case with booking id with 12345")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url= "https://restful-booker.herokuapp.com/booking/null"
    responseData= requests.get(url)
    assert responseData.status_code == 200