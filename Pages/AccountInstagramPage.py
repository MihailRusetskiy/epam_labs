import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utils.screen_of_element import get_element_screen
from Utils.helpers import *


class AccountInstagram(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/account/instagram"
        # локаторы
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

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.logger.info("Страница инстаграм аккаунты открыта")
        time.sleep(2)

    # возвращает все инстаграмм аккаунты
    def get_instagram_accounts(self):
        return self.driver.execute_script(
            open("../Utils/js/find_vk_instagram_accounts_on_page.js").read() + "return find('account_instagram_load');")

    # добавляет инстаграмм аккаунт с заданным логином и паролем
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
        self.logger.info("Инстаграмм аккаунт добавлен")

    # удаляет все инстаграмм аккаунты
    def remove_instagram_account(self):
        self.driver.find_element(*self._dropdown_select).click()
        time.sleep(1)
        self.driver.find_element(*self._select_all_button).click()
        self.driver.find_element(*self._delete_button).click()
        time.sleep(1)
        self.driver.find_element(*self._confirm_delete).click()
        time.sleep(2)
        self.logger.info("Все истаграмм аккаунты удалены")

    # воспроизводит видео справку
    def play_help_video(self):
        video = self.driver.find_element(*self._video)
        directory = "../Output/Screenshots/check_video"  # директория для скриншотов
        number_of_screenshots = 5  # количество скриншотов для проверки

        self.driver.find_element(*self._show_help_video_button).click()
        time.sleep(1)
        clear_directory(directory)  # очищаем папку
        video.click()  # запускаем видео
        self.logger.info("папка для скриншотов очищена, запуск видео")

        while number_of_screenshots:  # в цикле делаем скриншоты
            full_filename = get_filename(directory)  # получаем полное имя для нового скриншота
            self.screens.append(full_filename)  # добавляем скриншот в список сделанных скриншотов
            get_element_screen(self.driver, video, full_filename)  # делаем скриншот
            time.sleep(5)
            number_of_screenshots -= 1
            
        self.logger.info("скриншоты видео сохранены")
