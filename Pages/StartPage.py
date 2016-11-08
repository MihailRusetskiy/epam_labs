import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com"
        # локаторы
        self._balance_value = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//span[@class="total text-center"]')
        self._balance_label = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//span[@class="title text-center"]')
        self._balance_icon = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//i[@class="icon-wallet"]')

        self._tp_name = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="total text-center"]')
        self._tp_label = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="title text-center"]')
        self._tp_icon = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//i[@class="icon-bar-chart"]')

        self._paid_days_value = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//span[@class="total text-center"]')
        self._paid_days_label = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//span[@class="title text-center"]')
        self._paid_days_icon = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-3"]//i[@class="icon-clock"]')

        self._work_tasks_count_value = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="total text-center"]')
        self._work_tasks_count_label = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="title text-center"]')
        self._work_tasks_count_icon = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//i[@class="icon-rocket"]')

        self._added_counts_value = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="total text-center"]')
        self._added_counts_label = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//span[@class="title text-center"]')
        self._added_counts_icon = (
            By.XPATH, '//section[@id="main-content"]//div[@class="col-md-6"]//i[@class="icon-users"]')
        self._account_settings_dropdown = (By.CLASS_NAME, 'dropdown-toggle')
        self._logout_link = (By.ID, 'logout_link')
        self._confirm = (By.XPATH, '//div[@class="modal-dialog"]//button[contains(text(), "Да")]')

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.logger.info("открыта стартовая страница")

    # возвращает баланс
    def get_balance(self):
        self.driver.find_element(*self._balance_icon)
        self.logger.info("получен баланс на стартовой странице")
        return self.driver.find_element(*self._balance_value).text

    # возвращает тарифный план
    def get_tp(self):
        self.driver.find_element(*self._tp_icon)
        self.logger.info("получен тарифный план на стартовой странице")
        return self.driver.find_element(*self._tp_name).text

    # возвращает количество оплаченных дней
    def get_paid_days(self):
        self.driver.find_element(*self._paid_days_icon)
        return self.driver.find_elements(*self._paid_days_value)[1].text

    # возвращает текущее количество работающих задач
    def get_work_task(self):
        self.driver.find_element(*self._work_tasks_count_icon)
        return self.driver.find_elements(*self._work_tasks_count_value)[1].text

    # возвращает количество добавленных аккаунтов
    def get_added_counts(self):
        self.driver.find_element(*self._added_counts_icon)
        return self.driver.find_elements(*self._added_counts_value)[2].text

    # выход из системы
    def logout(self):
        self.driver.find_element(*self._account_settings_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*self._logout_link).click()
        time.sleep(1)
        self.driver.find_element(*self._confirm).click()
        time.sleep(1)
        self.logger.info("выход из системы")
