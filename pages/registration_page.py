from selene import have, command, be
from selene.support.shared import browser

import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.visible).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.visible).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.visible).type(value)
        return self

    def fill_gender(self):
        browser.element('label[for="gender-radio-1"]').should(be.visible).click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').should(be.visible).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choose_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def choose_hobbies(self):
        browser.element('label[for="hobbies-checkbox-2"]').click()
        return self

    def upload_image(self):
        browser.element('//input[@type="file"]').type(resource.path("image.jpg"))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def choose_state(self, value):
        browser.element('//*[@id="react-select-3-input"]').type(value).press_enter()
        return self

    def choose_city(self, value):
        browser.element('//*[@id="react-select-4-input"]').type(value).press_enter()
        return self

    def delete_footer(self):
        browser.element('//footer').perform(command.js.remove)
        return self

    def submit_form(self):
        browser.element('#submit').click()
        return self

    def should_registered_user_with(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby,
                                    picture, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                state,
                city
            )
        )
        return self
