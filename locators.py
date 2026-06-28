from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") #Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") #Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") #Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']") #Ссылка "Войти"
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']") #Сообщение об ошибке при вводе некорректного пароля

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") #Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") #Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") #Кнопка "Войти"
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']") #Ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']") #Ссылка "Восстановить пароль"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']") #Кнопка "Восстановить"
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']") #Ссылка "Войти"
    
class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']") #Ссылка "Личный кабинет"
    CONSTRUCTION_LINK = (By.CSS_SELECTOR, "a[href='/']") #Ссылка "Конструктор"
    LOGO = (By.XPATH, ".//a[@href='/']//*[name()='svg']") #Логотип Stellar Burgers
    BUNS_TAB = (By.XPATH, "//div[span[text()='Булки']]") #Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//div[span[text()='Соусы']]") #Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//div[span[text()='Начинки']]") #Вкладка "Начинки"
    BUNS_SECTION = (By.XPATH, ".//h2[text()='Булки']") #Заголовок "Булки"
    SAUCES_SECTION = (By.XPATH, ".//h2[text()='Соусы']") #Заголовок "Соусы"
    FILLINGS_SECTION = (By.XPATH, ".//h2[text()='Начинки']") #Заголовок "Начинки"

class PersonalAccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") #Кнопка "Выход"