import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import MainPageLocators, PersonalAccountLocators


class TestPersonalAccount:
    def test_go_to_personal_account(self, logged_in_user):
        driver = logged_in_user

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))

        assert "/account" in driver.current_url

    def test_go_to_constructor_from_personal_account(self, logged_in_user):
        driver = logged_in_user

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))

        driver.find_element(*MainPageLocators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL