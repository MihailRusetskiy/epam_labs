import unittest
from Steps.Steps import *
from Steps.AccountSteps import *
from Steps.SettingSteps import *


username = ""
password = ""

class SocialHammerTests(unittest.TestCase):

    def test_register(self):
        name = get_random_string(5)
        email = generate_random_emails(1, 7)[0]
        name = get_random_string(8)

        register(name, email, name)


    def test_set_activity(self):
        login(username, password)
        settings_active_page = change_active_state_button()
        self.assertTrue(is_active_state_button_changed(settings_active_page))


    def test_remove_vk_account(self):
        login(username, password)
        delete_vk_account()
        self.assertEqual(get_vk_accounts(), 'В таблице отсутствуют данные')


    def test_remove_instagram_account(self):
        login(username, password)
        delete_instagram_account()
        self.assertEqual(get_instagram_accounts(), 'В таблице отсутствуют данные')


    def test_check_useful_tools_page(self):
        login(username, password)
        self.assertTrue(is_useful_tools_page_present())


    def test_check_start_page(self):
        login(username, password)
        self.assertTrue(is_useful_tools_page_present())


    def test_check_start_page(self):
        login(username, password)
        self.assertTrue(is_summary_info_present())


    def test_check_play_help_video(self):
        login(username, password)
        self.assertTrue(check_help_play_video())


    def test_check_news_page(self):
        login(username, password)
        self.assertTrue(is_news_content_present())


    def test_limits(self):
        login(username, password)
        change_limits_state()
        self.assertTrue(is_limits_page_changed())


    def test_add_instagram_account(self):
        account = get_random_string(5)
        pwd = get_random_string(5)

        login(username, password)
        add_instagram_account(account, pwd)
        self.assertEqual(get_instagram_accounts(), account)
    

    def test_add_vk_account(self):
        account = get_random_string(5)
        pwd = get_random_string(5)

        login(username, password)
        add_vk_account(account, pwd)
        self.assertEqual(get_vk_accounts(), account)
