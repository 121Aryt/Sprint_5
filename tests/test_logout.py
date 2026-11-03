import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import generate_login, generate_password
from locators import MainPageLocators, AuthPageLocators, PersonalAccountLocators

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture
def logged_in_user(driver):
    email = generate_login()
    password = generate_password()

    # Регистрация
    driver.get(BASE_URL + "register")
    driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Test Testov")
    driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    # Вход
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    
    return driver

def test_logout(logged_in_user):
    driver = logged_in_user
    time.sleep(2)
    
    # Переход в Личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
    
    # Нажимаем "Выход"
    driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
    
    # После выхода сайт редиректит на страницу входа
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url