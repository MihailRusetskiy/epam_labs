import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utils.screen_of_element import get_element_screen
from Utils.helpers import *


class AccountInstagram(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
        self._accounts_menu_item = (By.XPATH, '//a[@title="Аккаунты"]')
        self._instagram_menu_item = (By.XPATH, '//a[@title="Инстаграм"]')
        self._continue_modal_button = (By.XPATH, '//button[contains(text(), "Продолжить")]')
        self._input_login_modal = (By.XPATH, '//form[@id="form_account_add"]//input[@placeholder="Логин без @"]')
        self._input_password_modal = (By.XPATH, '//form[@id="form_account_add"]//input[@placeholder="Пароль"]')
        self._save_instagram_account = (By.XPATH, '//div[@class="modal-footer"]//button[2]')
        self._close_modal_button = (By.XPATH, '//div[@class="modal-footer"]//button')
        self._add_account_button = (By.CLASS_NAME, 'action_account_add')
        self._dropdown_select = (By.XPATH, '//button[contains(text(), "Выделить")]')
        self._select_all_button = (By.XPATH, '//a[contains(text(), "Выбрать все")]')
        self._delete_button = (By.CLASS_NAME, 'action_account_destroy')
        self._confirm_delete = (By.CLASS_NAME, 'onConfirmYes')
        self._show_help_video_button = (By.CLASS_NAME, 'fa-question-circle')
        self._video = (By.XPATH, '//div[@id="window_modal"]//div[@class="modal-body"]')

        self.screens = []

    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.driver.find_element(*self._accounts_menu_item).click()
        time.sleep(1)
        self.driver.find_element(*self._instagram_menu_item).click()
        time.sleep(2)

    def get_instagram_accounts(self):
        return self.driver.execute_script(
            open("../Utils/js/find_vk_instagram_accounts_on_page.js").read() + "return find('account_instagram_load');")

    def add_instagram_account(self, account, password):
        self.driver.find_element(*self._add_account_button).click()
        time.sleep(1)
        self.driver.find_element(*self._continue_modal_button).click()
        time.sleep(1)
        self.driver.find_element(*self._input_login_modal).send_keys(account)
        self.driver.find_element(*self._input_password_modal).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self._save_instagram_account).click()
        time.sleep(1)
        self.driver.find_element(*self._close_modal_button).click()

    def remove_instagram_account(self):
        self.driver.find_element(*self._dropdown_select).click()
        time.sleep(1)
        self.driver.find_element(*self._select_all_button).click()
        self.driver.find_element(*self._delete_button).click()
        time.sleep(1)
        self.driver.find_element(*self._confirm_delete).click()
        time.sleep(2)

    def play_help_video(self):
        video = self.driver.find_element(*self._video)
        directory = "../Output/Screenshots/check_video"
        number_of_screenshots = 5

        self.driver.find_element(*self._show_help_video_button).click()
        time.sleep(1)
        clear_directory(directory)
        video.click()

        while number_of_screenshots:
            full_filename = get_filename(directory)
            self.screens.append(full_filename)
            get_element_screen(self.driver, video, full_filename)
            time.sleep(5)
            number_of_screenshots -= 1
