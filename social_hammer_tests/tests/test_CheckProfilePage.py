import unittest
import time
from helpers.helpers import *


class CheckProfilePage(unittest.TestCase):

    def test_check_profile_page(self):

        driver = register()

        header_found = 0
        current_balance_title_found = 0
        tp_block_found = 0

        dropdown_button = driver.find_element_by_class_name("dropdown-toggle")
        dropdown_button.click()

        time.sleep(1)
        profile_button = driver.find_element_by_class_name("dropdown-menu").find_element_by_tag_name("li")
        profile_button.click()

        time.sleep(1)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Профиль":
            header_found = 1

        balance_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[1]
        balance_block.find_element_by_class_name("icon-wallet")
        current_balance = balance_block.find_elements_by_class_name("text-center")[0].text
        if current_balance.find("Ваш баланс: $")+1:
            current_balance_title_found = 1

        tp_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[2]
        tp_block.find_element_by_class_name("icon-bar-chart")
        tp_sub_title = tp_block.find_elements_by_class_name("text-center")[1].text
        if tp_sub_title == "Тарифный план":
            tp_block_found = 1
        tp_sub_sub_title = tp_block.find_elements_by_class_name("text-center")[3].text
        if tp_sub_sub_title.find("Ограничение на количество задач:") +1:
            if tp_block_found:
                tp_block_found = 1
            else:
                tp_block_found = 0

        login_block = driver.find_element_by_id("main-content").find_elements_by_class_name("col-md-12")[3]
        login_block.find_element_by_class_name("icon-users")
        login_title = login_block.find_element_by_class_name("text-center").text
        if login_title.find("Текущий логин для входа в систему:")+1:
            login_found = 1

        self.assertTrue(current_balance_title_found and header_found and tp_block_found)

        driver.quit()
