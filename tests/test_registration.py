import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from data import generate_login, generate_password
from locators import AuthPageLocators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Test Testov")
        driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(generate_login())
        driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_incorrect_password_registration(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Test Testov")
        driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(generate_login())
        driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthPageLocators.PASSWORD_ERROR_MESSAGE)
        )
        assert error.is_displayed()