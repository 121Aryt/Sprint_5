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

def test_go_to_personal_account(logged_in_user):
    driver = logged_in_user
    time.sleep(2)
    
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
    assert "/account" in driver.current_url

def test_go_to_constructor_from_personal_account(logged_in_user):
    driver = logged_in_user
    time.sleep(2)
    
    # 1. Переход в Личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
    
    # 2. Переход в Конструктор
    driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL
    
    # 3. Возврат в Личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PersonalAccountLocators.PROFILE_SECTION))
    
    # 4. Переход по логотипу на главную
    driver.find_element(*MainPageLocators.LOGO_STELLAR_BURGERS).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL