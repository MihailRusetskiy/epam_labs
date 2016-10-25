from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com/login"
        self._input_email = (By.XPATH, '//input[@name="email"]')
        self._input_password = (By.XPATH, '//input[@name="password"]')
        self._login_button = (By.CLASS_NAME, 'col-xs-offset-2')
        self._dropdown = (By.CLASS_NAME, 'dropdown-toggle')
        self._login_on_mainpage = (By.XPATH, '//span[@class="test"]')

    def OpenPage(self):
        self.driver.get(self.BASE_URL)

    def Login(self, login, password):
        self.driver.find_element(*self._input_email).send_keys(login)
        self.driver.find_element(*self._input_password).send_keys(password)
        self.driver.find_element(*self._login_button).click()

    def GetCurrentLogin(self):
        return self.driver.find_element(*self._dropdown).find_element(*self._login_on_mainpage).text
