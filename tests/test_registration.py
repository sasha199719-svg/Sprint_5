from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from helpers import *
from locators import RegistrationPageLocators, LoginPageLocators 

def test_registration(driver):
    driver.get(BASE_URL + "register")
   
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(generate_user())
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.url_contains("login"))
    assert "login" in driver.current_url

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

def test_registration_short_password(driver):
    driver.get(BASE_URL + "register")

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(generate_user())
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
    assert error.text == "Некорректный пароль"