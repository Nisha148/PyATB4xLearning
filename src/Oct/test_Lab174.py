import pytest

def test_sub0():
    assert 2-2==0

def test_sub1():
    assert 3-3==0

def test_sub2():
    assert 1-1==0

@pytest.mark.skip(reason="Not completed,skip it")
def test_sub3():
    assert 0-0 !=0