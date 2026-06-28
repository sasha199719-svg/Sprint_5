from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL
from locators import MainPageLocators
from helpers import open_main

def test_switch_to_sauces(driver):
    open_main(driver)

    driver.find_element(*MainPageLocators.SAUCES_TAB).click()

    section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SAUCES_SECTION))

    assert section.is_displayed()


def test_switch_to_fillings(driver):
    open_main(driver)

    driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

    section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_SECTION))

    assert section.is_displayed()


def test_switch_to_buns(driver):
    open_main(driver)

    driver.find_element(*MainPageLocators.SAUCES_TAB).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()

    section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION))

    assert section.is_displayed()