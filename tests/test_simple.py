import allure

@allure.story('hello')
def test_1():
    assert True

@allure.story('hello32')
def test_2():
    assert True

@allure.title('asdsadasd')
def test_3():
    assert True

def test_4():
    assert True

@allure.title('hello213213')
def test_5():
    assert True