import unittest
import time
from helpers.helpers import *


class CheckUsefulToolsPageXpath(unittest.TestCase):

    def test_check_useful_tools_page_xpath(self):
        header_found = 0
        body_content_found = 0

        driver = register()

        utools = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[10]/a')
        utools.click()

        time.sleep(1)
        page_header = driver.find_element_by_xpath('//*[@id="main-wrapper"]/section/div/h1').text
        if page_header == "Полезные инструменты":
            header_found = 1

        body_content = driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div/div/div/div/table').text
        if body_content != "":
            body_content_found = 1

        self.assertTrue(header_found and body_content_found)

        driver.quit()
