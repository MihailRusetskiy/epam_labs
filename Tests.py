import unittest
from Steps.Steps import *
from Steps.AccountSteps import *
from Steps.SettingSteps import *

username = ""
password = ""


class SocialHammerTests(unittest.TestCase):

    def test1_register(self):
        name = get_random_string(5)
        email = generate_random_email(7)
        phone = get_random_string(8)

        register(name, email, phone)
        self.assertTrue(is_logged(name))

    def test2_set_activity(self):
        login(username, password)
        settings_active_page = change_active_state_button()
        self.assertTrue(is_active_state_button_changed(settings_active_page))

    def test3_remove_vk_account(self):
        login(username, password)
        delete_vk_account()
        self.assertEqual(get_vk_accounts(), 'В таблице отсутствуют данные')

    def test4_remove_instagram_account(self):
        login(username, password)
        delete_instagram_account()
        self.assertEqual(get_instagram_accounts(), 'В таблице отсутствуют данные')

    def test5_add_instagram_account_to_white_list(self):
        account = get_random_string(5)

        login(username, password)
        add_account_to_instagram_white_list(account)
        self.assertEqual(account, get_instagram_white_accounts())

    def test6_check_useful_tools_page(self):
        login(username, password)
        self.assertTrue(is_useful_tools_page_present())

    def test7_check_start_page(self):
        login(username, password)
        self.assertTrue(is_summary_info_present())

    def test8_check_play_help_video(self):
        login(username, password)
        self.assertTrue(check_help_play_video())

    def test9_check_news_page(self):
        login(username, password)
        self.assertTrue(is_news_content_present())

    def test_10_limits(self):
        login(username, password)
        change_limits_state()
        self.assertTrue(is_limits_page_changed())

    def test_11_add_instagram_account(self):
        account = get_random_string(5)
        pwd = get_random_string(5)

        login(username, password)
        add_instagram_account(account, pwd)
        self.assertEqual(get_instagram_accounts(), account)

    def test_12_add_instagram_account_to_white_list(self):
        account = get_random_string(5)

        login(username, password)
        add_account_to_instagram_white_list(account)
        self.assertEqual(account, get_instagram_white_accounts())

    def test_13_add_vk_account(self):
        account = get_random_string(5)
        pwd = get_random_string(5)

        login(username, password)
        add_vk_account(account, pwd)
        self.assertEqual(get_vk_accounts(), account)

    def test_14_check_profile_page(self):
        login(username, password)
        self.assertTrue(is_profile_page_balance_block_present() and is_profile_page_tp_block_present() and is_profile_page_settings_block_present())

    def test_15_logout(self):
        login(username, password)
        logout()
        dispose_driver()
        self.assertFalse(is_logged(username))
