from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    CONSTRUCTOR_TAB = (By.XPATH, "//*[contains(text(), 'Конструктор')]")
    LOGO_STELLAR_BURGERS = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")
    BUNS_SECTION = (By.XPATH, "//*[contains(text(), 'Булки')]")
    SAUCE_SECTION = (By.XPATH, "//*[contains(text(), 'Соусы')]")
    FILLINGS_SECTION = (By.XPATH, "//*[contains(text(), 'Начинки')]")

class AuthPageLocators:
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")
    LOGIN_BUTTON_IN_REGISTER_FORM = (By.XPATH, "//*[contains(text(), 'Войти')]")
    LOGIN_BUTTON_IN_RECOVERY_FORM = (By.XPATH, "//*[contains(text(), 'Войти')]")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//*[contains(text(), 'Войти')]")

class PersonalAccountLocators:
    PROFILE_SECTION = (By.XPATH, "//*[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Выход')]")