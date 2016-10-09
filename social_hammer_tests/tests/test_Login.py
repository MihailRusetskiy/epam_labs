import unittest
import time
from helpers.helpers import *


class Login(unittest.TestCase):

    def test_login(self):
        from helpers.helpers import domain
        username = ""
        password = ""

        driver = create_webdriver()
        driver.get(domain)

        login_input = driver.find_elements_by_class_name("form-control")[0]
        login_input.send_keys(username)

        password_input = driver.find_elements_by_class_name("form-control")[1]
        password_input.send_keys(password)

        login_button = driver.find_element_by_class_name("btn-block")
        login_button.click()

        time.sleep(1)
        page_header_text = driver.find_element_by_class_name("pageheader").text.strip()

        self.assertEqual(page_header_text, "Сводная информация")

        driver.quit()
