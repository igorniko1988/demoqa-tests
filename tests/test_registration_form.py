from selene.support.shared import browser
from selene import have, be, by
from selenium.webdriver import Keys
from selene import command
from pathlib import Path

from demoqa_tests.pages.registration import registration


def test_can_register_new_user():
    browser.open("automation-practice-form")

    browser.element("footer").execute_script("element.remove()")
    browser.element("/html/body/div[1]").execute_script("element.remove()")

    browser.element("#firstName").type("Igor")
    browser.element("#lastName").type("Niko")
    browser.element("#userEmail").type("niko@gmail.com")

    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("80632138412")
    browser.element("#dateOfBirthInput").perform(command.select_all).type(
        "14jun1988"
    ).with_(timeout=1).press_enter()
    browser.element(".subjects-auto-complete__control").element(
        "#subjectsInput"
    ).send_keys("Math").with_(timeout=1).press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element("#uploadPicture").send_keys(
        str(Path(__file__).parent.parent.joinpath("resourses", "test_file.txt"))
    )
    browser.element("#currentAddress").type("lorem ipsum")
    browser.element("#state").click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.text("Haryana")
    ).click()

    browser.element("#city").click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.text("Karnal")
    ).click()
    browser.element("#submit").click()
    browser.all(".table tbody tr td:nth-child(2)").should(
        have.texts(
            "Igor Niko",
            "niko@gmail.com",
            "Male",
            "8063213841",
            "14 June,1988",
            "Maths",
            "Sports",
            "test_file.txt",
            "lorem ipsum",
            "Haryana Karnal",
        )
    )


def test_user_can_register(user):
    registration.open("automation-practice-form").\
        fill_firstname(user.firstname).\
        fill_lastname(user.lastname).\
        fill_email(user.useremail).\
        fill_date_of_birth(user.dateofbirth).\
        fill_phone_number(user.usernumber).\
        chose_gender("Male").\
        chosoe_subjecet("Math").\
        choose_hobbies("Sports").\
        choose_state(user.state).\
        choose_city(user.city).\
        upload_picture(user.picture).\
        fill_current_addres(user.text).\
        submit()

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
