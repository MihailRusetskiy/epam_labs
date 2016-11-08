import random
import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AccountVk(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/account/vk"
        # локаторы
        self._accounts_menu_item = (By.XPATH, '//a[@title="Аккаунты"]')
        self._vk_menu_item = (By.XPATH, '//a[@title="Вконтакте"]')
        self._dropdown_select = (By.XPATH, '//button[contains(text(), "Выделить")]')
        self._select_all_button = (By.XPATH, '//a[contains(text(), "Выбрать все")]')
        self._delete_button = (By.CLASS_NAME, 'action_account_destroy')
        self._confirm_delete = (By.CLASS_NAME, 'onConfirmYes')
        self._add_account_button = (By.CLASS_NAME, 'action_account_add')
        self._continue_modal_button = (By.XPATH, '//button[contains(text(), "Продолжить")]')
        self._add_one_vk_account = (By.CLASS_NAME, 'action_account_add_one')
        self._input_login_modal = (By.XPATH, '//form[@id="form_account_add"]//input[@name="login"]')
        self._input_password_modal = (By.XPATH, '//form[@id="form_account_add"]//input[@placeholder="Пароль"]')
        self._save_vk_account = (By.XPATH, '//div[@class="modal-footer"]//button[2]')
        self._close_modal_button = (By.XPATH, '//div[@class="modal-footer"]//button')

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        self.logger.info("Страница аккаунты вконтакте открыта")

    # возвращает все вконтакте аккаунты на странице
    def get_vk_accounts(self):
        return self.driver.execute_script(
            open("../Utils/js/find_vk_instagram_accounts_on_page.js").read() + "return find('account_vk_load');")

    # добавляет вконтакте аккаунт с задаными логином и паролем
    def add_vk_account(self, account, password):
        self.driver.find_element(*self._add_account_button).click()
        time.sleep(1)
        self.driver.find_element(*self._add_one_vk_account).click()
        time.sleep(2)
        self.driver.find_element(*self._continue_modal_button).click()
        time.sleep(2)
        self.driver.find_element(*self._input_login_modal).send_keys(account)
        self.driver.find_element(*self._input_password_modal).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self._save_vk_account).click()
        time.sleep(1)
        self.driver.find_element(*self._close_modal_button).click()
        self.logger.info("аккаунт вконтакте добавлен")


    # удаляет все вконтакте аккаунты
    def remove_vk_account(self):
        self.driver.find_element(*self._dropdown_select).click()
        time.sleep(1)
        self.driver.find_element(*self._select_all_button).click()
        self.driver.find_element(*self._delete_button).click()
        time.sleep(1)
        self.driver.find_element(*self._confirm_delete).click()
        time.sleep(2)
        self.logger.info("все вконтакте аккаунты удалены")
