import os

from selene.support.shared import browser
from selene import have


def test_automation_practice_form():
    browser.open('/automation-practice-form')

    browser.element('[id="firstName"]').type('Denis')
    browser.element('[id="lastName"]').type('Mironov')
    browser.element('[id="userEmail"]').type('test@mail.ru')
    browser.element('[id="userNumber"]').type('9601234578')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="8"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1989"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('e').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath(r'fixtures\picture_1.jpg'))
    browser.element('[id="currentAddress"]').type('My address')
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('Delhi').click().press_enter()
    browser.element('[id="submit"]').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Denis Mironov',
        'test@mail.ru',
        'Male',
        '9601234578',
        '01 September,1989',
        'English',
        'Sports',
        'picture_1.jpg',
        'My address',
        'NCR Delhi'))
