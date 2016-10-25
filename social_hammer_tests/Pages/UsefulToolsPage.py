import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class UsefulToolsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://new.socialhammer.com"
        self._useful_tools_page_menu_item = (By.XPATH, '//a[@title="Полезные инструменты"]')
        self._page_header = (By.CLASS_NAME, 'pageheader')
        self._content_block = (By.ID, 'main-content')

    def open_page(self):
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*self._useful_tools_page_menu_item).click()
        time.sleep(1)

    def is_header_present(self):
        return self.driver.find_element(*self._page_header).text =='Полезные инструменты'

    def is_content_present(self):
        return self.driver.find_element(*self._content_block).text != ''



