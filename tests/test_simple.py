import pytest
import allure

@allure.step('teswt2')
def test_1():
    assert True

@allure.step('teswt2')
def test_2():
    assert True



@allure.step('teswt2')
def test_3():
    assert True

@allure.step('asdasd')
def test_4():
    assert True

def test_5():
    assert True

@pytest.mark.skip('aa')
def test_skip():
    pass

@pytest.mark.skip('a2a')
def test_skip2():
    pass

@pytest.mark.skip('a3a')
def test_skip3():
    pass