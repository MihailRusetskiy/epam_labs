from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
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

    def open_page(self):
        self.driver.get(self.BASE_URL)

    def get_balance(self):
        self.driver.find_element(*self._balance_icon)
        return self.driver.find_element(*self._balance_value).text

    def get_tp(self):
        self.driver.find_element(*self._tp_icon)
        return self.driver.find_element(*self._tp_name).text

    def get_paid_days(self):
        self.driver.find_element(*self._paid_days_icon)
        return self.driver.find_elements(*self._paid_days_value)[1].text

    def get_work_task(self):
        self.driver.find_element(*self._work_tasks_count_icon)
        return self.driver.find_elements(*self._work_tasks_count_value)[1].text

    def get_added_counts(self):
        self.driver.find_element(*self._added_counts_icon)
        return self.driver.find_elements(*self._added_counts_value)[2].text





