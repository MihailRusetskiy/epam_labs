import unittest
import time
from helpers.helpers import *


class CheckStartPage(unittest.TestCase):

    def test_check_start_page(self):
        driver = register()

        header_is_present = 0
        balance_found = 0
        tp_found = 0
        paid_days_found = 0
        tasks_found = 0
        accounts_found = 0

        menu_settings = driver.find_element_by_class_name("nav-pills").find_elements_by_tag_name("li")[0]
        menu_settings.click()

        time.sleep(2)
        page_header = driver.find_element_by_class_name("pageheader").text
        if page_header == "Сводная информация":
            header_is_present = 1

        main_content_div = driver.find_element_by_id("main-content")

        balance_block = main_content_div.find_element_by_class_name("col-md-3")
        balance_block.find_element_by_class_name("icon-wallet")
        balance = balance_block.find_element_by_class_name("total").text
        if balance.find("$")+1:
            balance_found = 1
        balance_title = balance_block.find_element_by_class_name("title").text
        if balance_title != "Ваш баланс":
            balance_found = 0

        tp_block = main_content_div.find_element_by_class_name("col-md-6")
        tp_block.find_element_by_class_name("icon-bar-chart")
        tp_title = tp_block.find_element_by_class_name("title").text
        if tp_title == "Тарифный план":
            tp_found = 1

        paid_days_block = main_content_div.find_elements_by_class_name("col-md-3")[1]
        paid_days_block.find_element_by_class_name("icon-clock")
        int(paid_days_block.find_element_by_class_name("total").text)
        paid_days_title = paid_days_block.find_element_by_class_name("title").text
        if paid_days_title == "Оплаченных дней":
            paid_days_found = 1

        tasks_work_block = main_content_div.find_elements_by_class_name("col-md-6")[1]
        tasks_work_block.find_element_by_class_name("icon-rocket")
        int(tasks_work_block.find_element_by_class_name("total").text)
        tasks_title = tasks_work_block.find_element_by_class_name("title").text
        if tasks_title == "Работающих задач":
            tasks_found = 1

        added_accounts = main_content_div.find_elements_by_class_name("col-md-6")[2]
        added_accounts.find_element_by_class_name("icon-users")
        int(added_accounts.find_element_by_class_name("total").text)
        accounts_title = added_accounts.find_element_by_class_name("title").text
        if accounts_title.find("Добавлен") + 1 > 0:
            accounts_found = 1

        self.assertTrue(accounts_found and balance_found and tp_found and tasks_found and paid_days_found and header_is_present)

        driver.quit()
