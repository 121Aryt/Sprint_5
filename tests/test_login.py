import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import MainPageLocators, AuthPageLocators


class TestLogin:
    def test_login_via_main_button(self, driver, test_user):
        email, password = test_user
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
        driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_personal_account_button(self, driver, test_user):
        email, password = test_user
        driver.delete_all_cookies()
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON))

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
        driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_register_form_button(self, driver, test_user):
        email, password = test_user
        driver.get(BASE_URL + "register")

        # ИСПОЛЬЗУЕМ УТОЧНЕННЫЙ ЛОКАТОР ДЛЯ ССЫЛКИ
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK_IN_REGISTER)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
        driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_recovery_form_button(self, driver, test_user):
        email, password = test_user
        driver.get(BASE_URL + "forgot-password")

        # ИСПОЛЬЗУЕМ УТОЧНЕННЫЙ ЛОКАТОР ДЛЯ ССЫЛКИ
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_LINK_IN_RECOVERY)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
        driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL