import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import MainPageLocators, PersonalAccountLocators


class TestLogout:
    def test_logout(self, logged_in_user):
        driver = logged_in_user

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))

        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url