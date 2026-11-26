import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import MainPageLocators


class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGO_STELLAR_BURGERS))
        
        tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION))
        driver.execute_script("arguments[0].click();", tab)

        # ПРОВЕРКА РЕЗУЛЬТАТА ЧЕРЕЗ H2 (требование наставника)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER))
        assert driver.find_element(*MainPageLocators.BUNS_HEADER).is_displayed()

    def test_switch_to_sauce_section(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGO_STELLAR_BURGERS))
        
        tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SAUCE_SECTION))
        driver.execute_script("arguments[0].click();", tab)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SAUCE_HEADER))
        assert driver.find_element(*MainPageLocators.SAUCE_HEADER).is_displayed()

    def test_switch_to_fillings_section(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGO_STELLAR_BURGERS))
        
        tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION))
        driver.execute_script("arguments[0].click();", tab)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_HEADER))
        assert driver.find_element(*MainPageLocators.FILLINGS_HEADER).is_displayed()