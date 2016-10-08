import time
import unittest
from helpers.helpers import *
from .test_AddInstagramAccount import add_instagram_account


class RemoveInstagramAccount(unittest.TestCase):

    def test_remove_instagram_account(self):

        driver = register()
        ai = add_instagram_account(driver)

        select_button = driver.find_element_by_class_name("panel-heading").find_element_by_class_name(
            "btn-group").find_element_by_class_name("dropdown-toggle")
        select_button.click()

        time.sleep(1)
        select_all_button = driver.find_element_by_class_name("panel-heading").find_element_by_class_name(
            "action_select_all")
        select_all_button.click()

        time.sleep(1)
        delete_acc_button = driver.find_element_by_class_name("action_account_destroy")
        delete_acc_button.click()

        time.sleep(2)
        confirm_delete_button = driver.find_element_by_id("window_modal").find_element_by_class_name("onConfirmYes")
        confirm_delete_button.click()

        time.sleep(4)
        added_account = driver.execute_script(
            open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
            "return find('account_instagram_load');")

        self.assertEqual(added_account, 'В таблице отсутствуют данные')

        driver.quit()
