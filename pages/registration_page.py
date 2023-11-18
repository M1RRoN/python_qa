import resource
from selene import browser, be, have, command


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def register(self, user):
        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').should(be.visible).type(user.last_name)
        browser.element('#userEmail').should(be.visible).type(user.email)
        browser.all('label[for="gender-radio-1"]').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').should(be.visible).type(user.phone_number)
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').type(user.month_of_birth)
        browser.element('.react-datepicker__year-select').type(user.year_of_birth)
        browser.element(
            f'.react-datepicker__day--0{user.day_of_birth}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobby)).click()
        browser.element('#uploadPicture').should(be.visible).type(resource.path(user.picture))
        browser.element('#currentAddress').should(be.visible).type(user.current_address)
        browser.element("#react-select-3-input").should(be.visible).type(user.state).press_enter()
        browser.element("#react-select-4-input").should(be.visible).type(user.city).press_enter()
        browser.element("#submit").should(be.visible).click()
        return self

    def user_should_registered(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.city}'
        ))
        return self
