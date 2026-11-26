from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    CONSTRUCTOR_TAB = (By.XPATH, "//*[contains(text(), 'Конструктор')]")
    LOGO_STELLAR_BURGERS = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")
    
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Булки']]")
    SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Начинки']]")
    
    # ПРОВЕРКА ТАБОВ ЧЕРЕЗ H2 (как просил наставник)
    BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCE_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]")


class AuthPageLocators:
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")
    
    # УТОЧНЕННЫЕ ЛОКАТОРЫ ДЛЯ "ВОЙТИ"
    # На страницах регистрации и восстановления это ссылка <a>
    LOGIN_LINK_IN_REGISTER = (By.XPATH, "//a[contains(text(), 'Войти')]")
    LOGIN_LINK_IN_RECOVERY = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # На странице входа это кнопка <button>
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Некорректный пароль') or contains(text(), 'Неверный пароль')]")


class PersonalAccountLocators:
    PROFILE_SECTION = (By.XPATH, "//*[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Выход')]")