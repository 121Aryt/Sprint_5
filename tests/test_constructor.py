from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import MainPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"

def test_switch_to_buns_section(driver):
    driver.get(BASE_URL)
    element = driver.find_element(*MainPageLocators.BUNS_SECTION)
    ActionChains(driver).move_to_element(element).click().perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Булки']")))
    assert driver.find_element(*MainPageLocators.BUNS_SECTION).is_displayed()

def test_switch_to_sauce_section(driver):
    driver.get(BASE_URL)
    element = driver.find_element(*MainPageLocators.SAUCE_SECTION)
    ActionChains(driver).move_to_element(element).click().perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Соусы']")))
    assert driver.find_element(*MainPageLocators.SAUCE_SECTION).is_displayed()

def test_switch_to_fillings_section(driver):
    driver.get(BASE_URL)
    element = driver.find_element(*MainPageLocators.FILLINGS_SECTION)
    ActionChains(driver).move_to_element(element).click().perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Начинки']")))
    assert driver.find_element(*MainPageLocators.FILLINGS_SECTION).is_displayed()