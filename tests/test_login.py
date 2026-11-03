import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import generate_login, generate_password
from locators import MainPageLocators, AuthPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture
def registered_user(driver):
    email = generate_login()
    password = generate_password()

    driver.get(BASE_URL + "register")
    driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Test Testov")
    driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    return email, password


def test_login_via_main_button(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL)
    time.sleep(2)

    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
    
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL


def test_login_via_personal_account_button(driver, registered_user):
    email, password = registered_user
    
    # Сбрасываем куки, чтобы гарантировать чистый старт
    driver.delete_all_cookies()
    driver.get(BASE_URL)
    time.sleep(2)

    # Находим и кликаем кнопку "Личный кабинет"
    account_btn = driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    driver.execute_script("arguments[0].click();", account_btn)
    
    # Ждём появления формы входа
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
    
    # Вводим данные и входим
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

    # === ИСПРАВЛЕНИЕ: после входа сайт редиректит на главную, а не в /account ===
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL


def test_login_via_register_form_button(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL + "register")
    time.sleep(2)

    driver.find_element(*AuthPageLocators.LOGIN_BUTTON_IN_REGISTER_FORM).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
    
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL


def test_login_via_recovery_form_button(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL + "forgot-password")
    time.sleep(2)

    driver.find_element(*AuthPageLocators.LOGIN_BUTTON_IN_RECOVERY_FORM).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
    
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL