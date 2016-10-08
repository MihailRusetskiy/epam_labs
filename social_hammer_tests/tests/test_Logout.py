import unittest
import time
from helpers.helpers import *


class Logout(unittest.TestCase):

    def test_logout(self):
        driver = register()

        dropdown_button = driver.find_element_by_class_name("dropdown-toggle")
        dropdown_button.click()

        time.sleep(1)
        profile_button = driver.find_element_by_class_name("dropdown-menu").find_elements_by_tag_name("li")[4]
        profile_button.click()

        time.sleep(2)
        submit_logout_button = driver.find_element_by_id("window_modal").find_element_by_class_name("onConfirmYes")
        submit_logout_button.click()

        time.sleep(2)
        driver.find_element_by_id("login-wrapper")

        self.assertTrue(1)

        driver.quit()
