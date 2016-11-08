import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.BASE_URL = "http://dev.socialhammer.com/news"
        # локаторы
        self._news_menu_item = (By.XPATH, '//a[@title="Новости"]')
        self._pageheader = (By.CLASS_NAME, 'pageheader')
        self._content = (By.ID, 'main-content')

    # открывает текущую страницу
    def open_page(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)
        self.logger.info("Страница новостей открыта")

    # возвращает содержимое хедера на странице
    def get_header(self):
        self.logger.info("получено содержимое заголовка новостной страницы")
        return self.driver.find_element(*self._pageheader).text

    # возвращает контент на странице
    def get_content(self):
        self.logger.info("получено содержимое блока контента страницы новостей")
        return self.driver.find_element(*self._content).text
