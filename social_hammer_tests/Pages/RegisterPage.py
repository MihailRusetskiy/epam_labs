import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
        self._confirm_rules_checkbox = (By.XPATH, '//input[@name="rules_confirm"]')
        self._start_registration_button = (By.XPATH, '//a[contains(text(), "Зарегистрироваться")]')
        self._input_name = (By.XPATH, '//input[@name="name"]')
        self._input_email = (By.XPATH, '//input[@name="email"]')
        self._input_phone = (By.XPATH, '//input[@name="phone"]')
        self._register_button = (By.XPATH, '//form//button[contains(text(), "Зарегистрироваться")]')
        self._dropdown = (By.CLASS_NAME, 'dropdown-toggle')
        self._login_on_mainpage = (By.XPATH, '//span[@class="test"]')

    def OpenPage(self):
        self.driver.get(self.BASE_URL)

    def Register(self, name, email, phone):
        self.driver.find_element(*self._start_registration_button).click()
        time.sleep(1)
        self.driver.find_element(*self._confirm_rules_checkbox).click()
        self.driver.find_element(*self._input_name).send_keys(name)
        self.driver.find_element(*self._input_email).send_keys(email)
        self.driver.find_element(*self._input_phone).send_keys(phone)
        self.driver.find_element(*self._register_button).click()

    def GetCurrentLogin(self):
        return self.driver.find_element(*self._dropdown).find_element(*self._login_on_mainpage).text
