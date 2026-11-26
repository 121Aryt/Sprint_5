import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import AuthPageLocators
from data import generate_login, generate_password


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def test_user():
    """Создает ОДНОГО тестового пользователя на весь сеанс тестирования."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запускаем скрыто для регистрации
    reg_driver = webdriver.Chrome(options=options)
    reg_driver.implicitly_wait(5)

    email = generate_login()
    password = generate_password()

    reg_driver.get(BASE_URL + "register")
    reg_driver.find_element(*AuthPageLocators.REGISTER_NAME_INPUT).send_keys("Test User")
    reg_driver.find_element(*AuthPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
    reg_driver.find_element(*AuthPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
    reg_driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

    WebDriverWait(reg_driver, 10).until(EC.url_contains("/login"))
    reg_driver.quit()
    
    return email, password


@pytest.fixture
def logged_in_user(driver, test_user):
    """Фикстура для авторизованного пользователя (использует данные test_user)."""
    email, password = test_user
    
    driver.get(BASE_URL + "login")
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    return driver