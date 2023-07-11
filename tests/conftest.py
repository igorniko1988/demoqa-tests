import pytest
from selene.support.shared import browser
from faker import Faker
from demoqa_tests.data.users import User
from selenium.webdriver import FirefoxOptions, ChromeOptions
import allure
from allure import attach, attachment_type
import json

@pytest.fixture(autouse=True)
def attach():
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)

    # HTML
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.PNG)

    # JSON
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)

@pytest.fixture(autouse=True)
def browser_config():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    browser.config.driver_options = options
    browser.config.base_url = "https://demoqa.com/"
    browser.config.driver_name = "chrome"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture(scope="function")
def user() -> User:
    fake = Faker()
    user = User(
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        useremail=fake.email(),
        gender=fake.random_element(elements=("Male", "Female")),
        hobbie=fake.random_element(elements=("Reading", "Sports", "Music")),
    )

    return user
