from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL, EMAIl, PASSWORD
from locators import LoginPageLocators, MainPageLocators, PersonalAccountPageLocators
from helpers import close_google_popup, login

def test_go_to_personal_account(driver: WebDriver):
    login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountPageLocators.LOGOUT_BUTTON))

    assert "account/profile" in driver.current_url

def test_go_to_constructor(driver):
    close_google_popup(driver)
    login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTION_LINK)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION))

    assert driver.current_url == BASE_URL


def test_go_to_constructor_by_logo(driver):
    close_google_popup(driver)
    login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGO)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION))

    assert driver.current_url == BASE_URL


def test_logout(driver):
    close_google_popup(driver)
    login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

    assert "login" in driver.current_url
