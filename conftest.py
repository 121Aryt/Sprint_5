import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def cleanup_and_delay(driver):
    """Очищает cookie ПЕРЕД тестом и делает паузу ПОСЛЕ теста."""
    # Очищаем cookie, чтобы каждый тест начинался как "неавторизованный" пользователь
    driver.delete_all_cookies()
    
    yield
    
    # Небольшая пауза, чтобы сайт успел обработать завершение
    time.sleep(2)