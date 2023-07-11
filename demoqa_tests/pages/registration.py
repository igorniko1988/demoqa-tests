from selene.support.shared import browser
from selene import command, have, by, be
from demoqa_tests.data.users import User
import allure


class Registration:

    @allure.step('Open demoqa page')
    @allure.severity('Blocker')
    def open(self, url):
        browser.open(url)
        browser.element("footer").execute_script("element.remove()")
        browser.element("/html/body/div[1]").execute_script("element.remove()")
        return self

    @allure.step('Register user')
    @allure.severity('Critical')
    def register(self, user: User):
        browser.element("#firstName").type(user.firstname)
        browser.element("#lastName").type(user.lastname)
        browser.element("#userEmail").type(user.useremail)
        browser.element('[for="gender-radio-1"]').click()
        browser.element("#userNumber").type(user.usernumber)
        browser.element("#dateOfBirthInput").perform(command.select_all).type(
            user.dateofbirth).with_(timeout=1).press_enter()
        browser.element(".subjects-auto-complete__control").element("#subjectsInput").\
            send_keys(user.subject).with_(timeout=1).press_tab()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element("#uploadPicture").send_keys(user.picture)
        browser.element("#currentAddress").type(user.text)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(have.text(user.state)).click()
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(have.text(user.city)).click()
        browser.element("#submit").click()

    @allure.step('Check registered user')
    def registered_user_should_be(
        self,
        firstname,
        lastname,
        email,
        gender,
        phonenumber,
        dob,
        subject,
        hobbie,
        picture,
        text,
        state,
        city,
    ):
        browser.all(".table tbody tr td:nth-child(2)").should(
            have.texts(
                firstname + " " + lastname,
                email,
                gender,
                phonenumber,
                dob,
                subject,
                hobbie,
                picture,
                text,
                state + " " + city,
            )
        )
        return self



registration = Registration()
