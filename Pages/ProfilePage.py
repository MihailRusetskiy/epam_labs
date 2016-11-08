import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/profile"
        # локаторы
        self._balance_block = (By.XPATH, '//section[@id="main-content"]//div[@class="col-md-12 col-lg-8"]//div[@class="row"]//div[@class="col-md-12"][1]')
        self._tp_block = (By.XPATH, '//section[@id="main-content"]//div[@class="col-md-12 col-lg-8"]//div[@class="row"]/div[@class="col-md-12"][3]')
        self._settings_block = (By.XPATH, '//section[@id="main-content"]//div[@class="col-md-12 col-lg-8"]//div[@class="row"][2]//div[@class="col-md-12"]')
        self._account_settings_dropdown = (By.CLASS_NAME, 'dropdown-toggle')
        self._profile_page_link = (By.XPATH, '//ul[@class="dropdown-menu animated fadeInRight"]//a')
        self._balance_icon = (By.CLASS_NAME, 'icon-wallet')
        self._balance_value = (By.XPATH, '//div[@class="row text-center"]//strong')
        self._balance_pay_button = (By.XPATH, '//button[@class="jSaleOrder btn btn-success"]')
        self._balance_add_discount = (By.XPATH, '//button[@class="btn btn-default action_balance_add_coupon"]')
        self._tp_icon = (By.CLASS_NAME, 'icon-bar-chart')
        self._tp_value = (By.XPATH, '//span[@class="total text-center"]')
        self._settings_change_login_button = (By.XPATH, '//button[@class="btn btn-success action_change_login"]')
        self._settings_change_password_button = (By.XPATH, '//button[@class="btn btn-success action_change_password"]')
        self._settings_delete_account_button = (By.XPATH, '//button[@class="btn btn-danger action_user_destroy"]')
        self._settings_icon = (By.CLASS_NAME, 'icon-users')

    # открывает текущую страницу в браузере
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.logger.info("Открыта страница профиля")

    # возвращает баланс на странице
    def get_balance(self):
        balance_block = self.driver.find_element(*self._balance_block)
        self.logger.info("получен баланс на странице профиля")
        return balance_block.find_element(*self._balance_value).text.split(":")[1].strip()
        
    # проверяет есть ли иконка баланса
    def is_balance_icon_present(self):
        balance_block = self.driver.find_element(*self._balance_block)
        return balance_block.find_element(*self._balance_icon) is not None

    # проверяет есть ли на странице кнопка пополнения баланса
    def is_balance_pay_button_present(self):
        balance_block = self.driver.find_element(*self._balance_block)
        return balance_block.find_element(*self._balance_pay_button) is not None

    # проверяет есть ли кнопка применить скидку
    def is_balance_discount_present(self):
        balance_block = self.driver.find_element(*self._balance_block)
        return balance_block.find_element(*self._balance_add_discount) is not None

    # возвращает тариф
    def get_tp(self):
        tp_block = self.driver.find_element(*self._tp_block)
        self.logger.info("получен тариф на странице профиля")
        return tp_block.find_element(*self._tp_value).text.strip()

    # проверяет есть ли на странице иконка тарифа
    def is_tp_icon_present(self):
        tp_block = self.driver.find_element(*self._tp_block)
        return tp_block.find_element(*self._tp_icon) is not None

    # есть ли на странице иконка настройки
    def is_settings_icon_present(self):
        settings_block = self.driver.find_element(*self._settings_block)
        return settings_block.find_element(*self._settings_icon) is not None

    # есть ли на странице кнопка изменить логин
    def is_settings_change_login_button_present(self):
        settings_block = self.driver.find_element(*self._settings_block)
        return settings_block.find_element(*self._settings_change_login_button) is not None

    # есть ли на странице кнопка изменить пароль
    def is_settings_change_password_button_present(self):
        settings_block = self.driver.find_element(*self._settings_block)
        return settings_block.find_element(*self._settings_change_password_button) is not None

    # есть ли на странице кнопка удалить аккаунт
    def is_settings_delete_account_button_present(self):
        settings_block = self.driver.find_element(*self._settings_block)
        return settings_block.find_element(*self._settings_delete_account_button) is not None
