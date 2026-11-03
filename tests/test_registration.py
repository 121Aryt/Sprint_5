from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import generate_login, generate_password
from locators import AuthPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"

def test_successful_registration(driver):
    driver.get(BASE_URL + "register")

    driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Иван Тестов")
    driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(generate_login())
    driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url

def test_incorrect_password_registration(driver):
    driver.get(BASE_URL + "register")

    driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Иван Тестов")
    driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(generate_login())
    driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Некорректный пароль') or contains(text(), 'Неверный пароль')]")
        )
    )
    assert error.is_displayed()