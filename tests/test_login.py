from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from helpers import *
from locators import (RegistrationPageLocators,LoginPageLocators,MainPageLocators)

def test_login_from_main_page(driver):
    email = generate_email()
    password = "1234567"

    driver.get(BASE_URL + "login")

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    assert driver.find_element(*MainPageLocators.LOGO).is_displayed()

def test_login_from_personal_account_button(driver):
    email = generate_email()
    password = "1234567"

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
   
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    assert driver.find_element(*MainPageLocators.LOGO).is_displayed()

def test_login_from_registration_form(driver):
    email = generate_email()
    password = "1234567"

    driver.get(BASE_URL + "register")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    assert driver.find_element(*MainPageLocators.LOGO).is_displayed()

def test_login_from_forgot_password(driver):
    email = generate_email()
    password = "1234567"

    driver.get(BASE_URL + "login")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    assert driver.find_element(*MainPageLocators.LOGO).is_displayed()