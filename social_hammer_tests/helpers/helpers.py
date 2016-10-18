import random
import string
import time
import os
from django.core.serializers import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from helpers.proxy import *


domain = "http://new.socialhammer.com"
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.ru", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def create_webdriver():
    try:
        driver = webdriver.Chrome('/usr/bin/chromedriver')


    except Exception:
        print("cant open navigator")

    else:
        return driver


def create_webdriver_with_proxy(host, port, login, password):
    try:
        proxyauth_plugin_path = create_proxyauth_extension(
            proxy_host=host,
            proxy_port=int(port),
            proxy_username=login,
            proxy_password=password
        )

        co = Options()
        co.add_extension(proxyauth_plugin_path)

        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=co)

    except Exception:
        print("cant open navigator")

    else:
        return driver


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]


def get_random_string(length):
    return get_random_name(letters, length)


def check_active_state_button(table_rows, button_state):
    for table_row in table_rows:
        table_tds = table_row.find_elements_by_tag_name("td")

        c = table_tds[1].find_element_by_tag_name("span").get_attribute("class")
        if table_tds[1].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:
            button_state.append(1)
        else: button_state.append(0)

        if table_tds[3].find_element_by_tag_name("span").get_attribute("class").find(" on") > 0:
            button_state.append(1)
        else: button_state.append(0)

    return button_state


def is_equals_button_lists(list1, list2):
    button_index = len(list1)
    compare_res = 1

    while button_index:
        button_index -= 1
        if list1[button_index] != list2[button_index]:
            compare_res = 0
            break

    return compare_res


def get_filename(directory):
    files = os.listdir(directory)
    images = filter(lambda x: x.endswith('.png'), files)

    curr_image_name = 0
    for image in images:
        try:
            i = int(image.split(".")[0])
            if i > curr_image_name:
                curr_image_name = i
        except Exception:
            continue

    return directory + "/" + str(curr_image_name+1) + ".png"


def clear_directory(directory):
    files = os.listdir(directory)
    images = filter(lambda x: x.endswith('.png'), files)

    for image in images:
        os.remove(directory + "/" + image)

    return 1


def call_func(func, driver, domain):
    return func(driver, domain)


def register():
    driver = create_webdriver()

    driver.get(domain)

    register_button = driver.find_element_by_class_name("btn-danger")
    register_button.click()

    agree_rules_checkbox = driver.find_element_by_class_name("checkbox").find_element_by_tag_name("input")
    agree_rules_checkbox.click()

    input_email = driver.find_elements_by_class_name("form-control")[1]
    input_email.send_keys(generate_random_emails(1, 7)[0])

    register_button = driver.find_elements_by_class_name("btn-block")[1]
    register_button.click()

    time.sleep(2)
    register_phone_button = driver.find_element_by_id("form_register_phone").find_element_by_class_name("btn-block")
    register_phone_button.click()

    time.sleep(2)

    return driver