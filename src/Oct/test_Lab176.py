import pytest
import allure

@allure.title("TC#1 verify that 2-2=0")
@allure.description("This is a smoke testcase which verify that 2-2=0")
@pytest.mark.smoke
def test_sub0():
    assert 2-2==0

@allure.title("TC#2 verify that 2+2=4")
@allure.description("This is a smoke testcase which verify that 2+2=4")
@pytest.mark.smoke
def test_add1():
    assert 2+2==0

@allure.title("TC#3 verify that 2*2=4")
@allure.description("This is a smoke testcase which verify that 2*2=4")
@pytest.mark.smoke
def test_mul3():
    assert 2*2==4

@allure.title("TC#4 verify that 2/2=1")
@allure.description("This is a smoke testcase which verify that 2/2=1")
@pytest.mark.smoke
def test_div4():
    assert 2/2==1

@allure.title("TC#5 verify that 2-2!=0")
@allure.description("This is a smoke testcase which verify that 2-2!=0")
@pytest.mark.sanity
def test_sub5():
    assert 2-2!=0



