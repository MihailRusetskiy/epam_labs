import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class UsefulToolsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/helpful_tools"
        # локаторы
        self._useful_tools_page_menu_item = (By.XPATH, '//a[@title="Полезные инструменты"]')
        self._page_header = (By.CLASS_NAME, 'pageheader')
        self._content_block = (By.ID, 'main-content')

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.logger.info("открыта страница полезные инструменты")

    # проверяет наличие хедера на странице
    def is_header_present(self):
        self.logger.info("получено содержимое хедера на странице полезные инструменты")
        return self.driver.find_element(*self._page_header).text =='Полезные инструменты'

    # проверяет наличие контента на странице
    def is_content_present(self):
        self.logger.info("получен контент на странице полезные инструменты")
        return self.driver.find_element(*self._content_block).text != ''
