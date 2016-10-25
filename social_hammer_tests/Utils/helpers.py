import random
import string
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from Utils.compare_images import MonitorPicture

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


def push_random_int(min, max, collection):
    n = random.randint(min, max)
    collection.append(n)
    return n


def compare_video_screens(screens):
    image_number = len(screens) - 1
    compare_images_res = 1

    while image_number:

        compare_images_res = MonitorPicture(screens[image_number], screens[image_number - 1])
        image_number -= 1
        if compare_images_res:
            break
    return compare_images_res
