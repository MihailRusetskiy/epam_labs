import time
from Utils.driver.DriverInstance import DriverInstance
from Utils.helpers import *
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.UsefulToolsPage import UsefulToolsPage
from Pages.StartPage import StartPage
from Pages.NewsPage import NewsPage


def get_driver():
    return DriverInstance.get_instance()


def dispose_driver():
    DriverInstance.get_instance().quit()


def login(login, password):
    login_page = LoginPage(get_driver())
    login_page.OpenPage()
    login_page.Login(login, password)


def is_logged(login):
    login_page = LoginPage(get_driver())
    return login_page.GetCurrentLogin() in login


def register():
    name = get_random_string(5)
    email = generate_random_emails(1, 7)[0]
    phone = get_random_string(8)

    register_page = RegisterPage(get_driver())
    register_page.OpenPage()
    register_page.Register(name, email, phone)


def is_useful_tools_page_present():
    useful_tools_page = UsefulToolsPage(get_driver())
    useful_tools_page.open_page()
    return useful_tools_page.is_header_present() and useful_tools_page.is_content_present()


def is_summary_info_present():
    start_page = StartPage(get_driver())
    start_page.open_page()
    balance = start_page.get_balance()
    tp = start_page.get_tp()
    paid_days = start_page.get_paid_days()
    work_task_count = start_page.get_work_task()
    added_account_count = start_page.get_added_counts()

    return balance and tp and paid_days and work_task_count and added_account_count


def is_news_content_present():
    news_page = NewsPage(get_driver())
    news_page.open_page()
    return news_page.get_header() != '' and news_page.get_content() != ''












