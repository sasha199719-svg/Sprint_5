import random
from data import BASE_URL, EMAIl, PASSWORD
from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_email():
    number = random.randint(1000, 9999)
    return f"testemail{number}@yandex.ru"

def generate_password():
    return "123456"

def generate_user():
    number = random.randint(1000, 9999)
    return f"TestUser{number}"

def open_main(driver):
    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.BUNS_TAB))

def close_google_popup(driver):
    try:
        driver.switch_to.alert.accept()
    except:
        pass

def login(driver):
    close_google_popup(driver)
    driver.get(BASE_URL + "login")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(EMAIl)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK))