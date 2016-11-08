import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/login"
        # локаторы
        self._input_email = (By.XPATH, '//input[@name="email"]')
        self._input_password = (By.XPATH, '//input[@name="password"]')
        self._login_button = (By.CLASS_NAME, 'col-xs-offset-2')
        self._dropdown = (By.CLASS_NAME, 'dropdown-toggle')
        self._login_on_mainpage = (By.XPATH, '//span[@class="text"]')

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.logger.info("страница ")

    # вход в сисетему по логину и паролю
    def login(self, login, password):
        self.driver.find_element(*self._input_email).send_keys(login)
        self.driver.find_element(*self._input_password).send_keys(password)
        self.driver.find_element(*self._login_button).click()
        time.sleep(2)
        self.logger.info("авторизация в системе")

    # пытается получить текущий логин
    # если элемента с логин нет то
    # возвращается пустая строка
    def get_current_login(self):
        try:
            self.driver.find_element(*self._dropdown)
        except Exception:
            self.logger.warning("не найден элемент с логином юзера")
            return ''
        else:
            self.logger.info("получен текущий логин пользователя")
            return self.driver.find_element(*self._dropdown).find_element(*self._login_on_mainpage).text
