import unittest
import time
from helpers.helpers import *


class CheckNewsPage(unittest.TestCase):

    def test_check_news_page(self):
        header_is_present = 0
        content_is_present = 0

        driver = register()

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[1]
        menu_settings.click()

        time.sleep(1)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Новости сервиса":
            header_is_present = 1

        page_content = driver.find_element_by_id("main-content").find_element_by_class_name("panel-default").text
        if page_content != "":
            content_is_present = 1

        self.assertTrue(content_is_present and header_is_present)

        driver.quit()
