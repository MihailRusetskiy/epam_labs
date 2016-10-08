import unittest
import time
from helpers.helpers import *


class CheckLimitsXpath(unittest.TestCase):

    def test_check_limits_xpath(self):
        res = 1
        instagram_like_value_n = 1
        instagram_following_value_n = 2
        instagram_unfollowing_value_n = 3
        vk_invitations_friends_value_n = 4
        vk_like_value_n = 5
        vk_invitations_group_friends_value_n = 6

        driver = register()

        menu_settings = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[7]/a')
        menu_settings.click()

        time.sleep(1)
        menu_limits = driver.find_element_by_xpath('//*[@id="main-wrapper"]/aside/nav/ul/li[7]/ul/li[2]/a')
        menu_limits.click()

        time.sleep(2)
        instagram_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[1]/label/input')
        instagram_is.click()

        instagram_like_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/label/input')
        instagram_like_is.click()

        instagram_following_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/label/input')
        instagram_following_is.click()

        instagram_unfollowing_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/label/input')
        instagram_unfollowing_is.click()

        vk_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[1]/label/input')
        vk_is.click()

        vk_invitations_friends_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/label/input')
        vk_invitations_friends_is.click()

        vk_like_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/label/input')
        vk_like_is.click()

        vk_invitations_group_friends_is = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/label/input')
        vk_invitations_group_friends_is.click()

        instagram_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/input')
        instagram_like_value.clear()
        instagram_like_value.send_keys(instagram_like_value_n)

        instagram_following_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/input')
        instagram_following_value.clear()
        instagram_following_value.send_keys(instagram_following_value_n)

        instagram_unfollowing_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/input')
        instagram_unfollowing_value.clear()
        instagram_unfollowing_value.send_keys(instagram_unfollowing_value_n)

        vk_invitations_friends_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/input')
        vk_invitations_friends_value.clear()
        vk_invitations_friends_value.send_keys(vk_invitations_friends_value_n)

        vk_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/input')
        vk_like_value.clear()
        vk_like_value.send_keys(vk_like_value_n)

        vk_invitations_group_friends_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/input')
        vk_invitations_group_friends_value.clear()
        vk_invitations_group_friends_value.send_keys(vk_invitations_group_friends_value_n)
        time.sleep(2)

        driver.refresh()

        time.sleep(1)

        instagram_like_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[2]/div/input')
        if instagram_like_value == str(instagram_like_value_n):
            is_instagram_like_value = 1

        instagram_following_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[3]/div/input').text
        if instagram_following_value == str(instagram_following_value_n):
            instagram_following_value = 1

        instagram_unfollowing_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[1]/div[4]/div/input').text
        if instagram_unfollowing_value == str(instagram_unfollowing_value_n):
            instagram_unfollowing_value = 1

        vk_invitations_friends_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[2]/div[2]/div/input').text
        if vk_invitations_friends_value == str(vk_invitations_friends_value_n):
            vk_invitations_friends_value = 1

        vk_like_value = driver.find_element_by_xpath('//*[@id="form_setting_account_limit_update"]/div[2]/div[3]/div/input').text
        if vk_like_value == str(vk_like_value_n):
            vk_like_value = 1

        vk_invitations_group_friends_value = driver.find_element_by_xpath(
            '//*[@id="form_setting_account_limit_update"]/div[2]/div[4]/div/input')
        if vk_invitations_group_friends_value == str(vk_invitations_group_friends_value_n):
            vk_invitations_group_friends_value = 1

        if vk_invitations_group_friends_value and vk_like_value and vk_invitations_friends_value and instagram_unfollowing_value and instagram_following_value and is_instagram_like_value:
            res = 1

        self.assertTrue(res)

        driver.quit()
