import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
        self._news_menu_item = (By.XPATH, '//a[@title="Новости"]')
        self._pageheader = (By.CLASS_NAME, 'pageheader')
        self._content = (By.ID, 'main-content')


    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.driver.find_element(*self._news_menu_item).click()
        time.sleep(1)

    def get_header(self):
        return self.driver.find_element(*self._pageheader).text

    def get_content(self):
        return self.driver.find_element(*self._content).text
