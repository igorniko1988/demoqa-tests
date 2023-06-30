from selene.support.shared import browser
from selene import have, be, by
from selenium.webdriver import Keys
from selene import command
from pathlib import Path
from demoqa_tests.pages.registration import registration

def test_user_can_register(user):
    registration.open("automation-practice-form")
    registration.register(user)
    registration.registered_user_should_be(
        user.firstname,
        user.lastname,
        user.useremail,
        "Male",
        user.usernumber,
        user.dateofbirth,
        "Maths",
        "Sports",
        "test_file.txt",
        "Meet push whole",
        user.state,
        user.city,
    )
