from Pages.SettingsActivityPage import SettingsActivityPage
import time
from Utils.helpers import *
from Steps.Steps import get_driver
from Pages.AccountVkPage import AccountVk
from Pages.AccountInstagramPage import AccountInstagram


# удаляет все вконтакте аккаунты на странице
def delete_vk_account():
    account_vk_page = AccountVk(get_driver())
    account_vk_page.open_page()
    account_vk_page.remove_vk_account()


# возвращает все вконтакте аккаунты
def get_vk_accounts():
    account_vk_page = AccountVk(get_driver())
    return account_vk_page.get_vk_accounts()


# удаляет все интасграм аккаунты на странице
def delete_instagram_account():
    account_instagram_page = AccountInstagram(get_driver())
    account_instagram_page.open_page()
    account_instagram_page.remove_instagram_account()


# возвращает все инстаграмм аккаунты на странице
def get_instagram_accounts():
    account_instagram_page = AccountInstagram(get_driver())
    return account_instagram_page.get_instagram_accounts()


# запускает видео справку на странице
def check_help_play_video():
    account_instagram_page = AccountInstagram(get_driver())
    account_instagram_page.open_page()
    account_instagram_page.play_help_video()
    return compare_video_screens(account_instagram_page.screens)


# добавляет инстаграмм аккаунт с заданными логином и паролем
def add_instagram_account(account, password):
    account_instagram_page = AccountInstagram(get_driver())
    account_instagram_page.open_page()
    account_instagram_page.add_instagram_account(account, password)


# добавляет вконтакте аккаунт с заданными логином и паролем
def add_vk_account(account, password):
    account_vk_page = AccountVk(get_driver())
    account_vk_page.open_page()
    account_vk_page.add_vk_account(account, password)
