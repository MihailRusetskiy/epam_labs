import unittest
import time
from helpers.helpers import *


class AddToWhiteList(unittest.TestCase):
    def test_add_to_white_list(self):

        driver = register()
        account = get_random_string(8)

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[13]
        menu_settings.click()

        time.sleep(1)
        activity_menu_item = menu_settings.find_elements_by_tag_name("li")[7]
        activity_menu_item.click()

        time.sleep(2)
        add_button = driver.find_element_by_id("main-content").find_element_by_class_name("dropdown-toggle")
        add_button.click()

        time.sleep(1)
        add_one = driver.find_element_by_id("main-content").find_element_by_class_name("action_add")
        add_one.click()

        time.sleep(2)
        input_login = driver.find_element_by_id("form_add").find_element_by_class_name("form-control")
        input_login.send_keys(account)
        add_modal_button = driver.find_element_by_id("window_modal").find_element_by_class_name("btn-primary")
        add_modal_button.click()

        time.sleep(3)
        added_account = driver.execute_script(
            open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
            "return find('setting_account_instagram_white_load');")

        time.sleep(3)
        self.assertEqual(added_account.strip(), account)

        driver.quit()
