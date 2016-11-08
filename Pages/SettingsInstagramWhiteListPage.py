import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SettingsInstagramWhiteListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/setting/account-instagram/white"
        # локаторы
        self._dropdown_add_account = (By.XPATH, '//button[@class="btn btn-success dropdown-toggle"]')
        self._add_one_account = (By.XPATH, '//a[contains(text(), "Один аккаунт")]')
        self._account_input = (By.XPATH, '//input[@name="login"]')
        self._confirm_account_add = (By.XPATH, '//div[@class="modal-dialog"]//button[contains(text(), "Да")]')

    # открывет текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.logger.info("открыта страница настроек белого списка для инстаграмм")

    # добавляет заданный аккаунт в белый список
    def add_account_to_instagram_white_list(self, account):
        self.driver.find_element(*self._dropdown_add_account).click()
        time.sleep(1)
        self.driver.find_element(*self._add_one_account).click()
        time.sleep(1)
        self.driver.find_element(*self._account_input).send_keys(account)
        self.driver.find_element(*self._confirm_account_add).click()
        time.sleep(3)
        self.logger.info("аккаунт был добавлен в белый список")

    # возвращает все аккаунты в белом списке
    def get_instagram_white_account(self):
        self.logger.info("попытка поучения аккаунтов в белом списке")
        return self.driver.execute_script(open("../Utils/js/find_vk_instagram_accounts_on_page.js").read() +
                                          "return find('setting_account_instagram_white_load');")
