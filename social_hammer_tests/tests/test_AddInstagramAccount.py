import unittest
import time
from helpers.helpers import *


def add_instagram_account(driver):
    account_name = get_random_string(5)
    accpunt_password = get_random_string(5)

    menu_accounts = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[3]
    menu_accounts.click()

    time.sleep(2)
    skip_intro_button = driver.find_element_by_class_name("introjs-button")
    skip_intro_button.click()

    time.sleep(1)
    add_instagram_menu_item = menu_accounts.find_elements_by_tag_name("a")[1]
    add_instagram_menu_item.click()

    time.sleep(2)
    button_add = driver.find_element_by_class_name("action_account_add")
    button_add.click()

    time.sleep(1)
    close_notification_no_proxy = driver.find_element_by_class_name("onConfirmClose")
    close_notification_no_proxy.click()

    time.sleep(2)
    modal_window = driver.find_element_by_class_name("modal-content")
    login_input = modal_window.find_elements_by_class_name("form-control")[0]
    login_input.send_keys(account_name)

    password_input = modal_window.find_elements_by_class_name("form-control")[1]
    password_input.send_keys(accpunt_password)

    dont_change_proxy_checkbox = modal_window.find_element_by_class_name("checkbox")
    dont_change_proxy_checkbox.click()

    add_instagram_acc = modal_window.find_element_by_class_name("btn-primary")
    add_instagram_acc.click()

    time.sleep(2)
    close_button = modal_window.find_element_by_class_name("btn-default")
    close_button.click()

    time.sleep(2)

    added_account = driver.execute_script(
        open("/home/hpx/PycharmProjects/bot/helpers/js/find_vk_instagram_accounts_on_page.js").read() +
        "return find('account_instagram_load');")

    if added_account == added_account:
        return 1
    else:
        return 0


class AddInstagramAccount(unittest.TestCase):

    def test_add_instagram_account(self):

        driver = register()

        res = add_instagram_account(driver)

        self.assertTrue(res)

        driver.quit()
