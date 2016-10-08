import time
import unittest
from helpers.helpers import *


class Register(unittest.TestCase):
    def test_register(self):

        driver = create_webdriver()
        driver.get(domain)

        register_button = driver.find_element_by_class_name("btn-danger")
        register_button.click()

        agree_rules_checkbox = driver.find_element_by_class_name("checkbox").find_element_by_tag_name("input")
        agree_rules_checkbox.click()

        input_email = driver.find_elements_by_class_name("form-control")[1]
        input_email.send_keys(generate_random_emails(1,7)[0])

        register_button = driver.find_elements_by_class_name("btn-block")[1]
        register_button.click()

        time.sleep(2)
        register_phone_button = driver.find_element_by_id("form_register_phone").find_element_by_class_name("btn-block")
        register_phone_button.click()

        time.sleep(2)
        page_header_text = driver.find_element_by_class_name("pageheader").text.strip()

        self.assertEqual(page_header_text, "Добро пожаловать в SocialHammer!")

        driver.quit()
