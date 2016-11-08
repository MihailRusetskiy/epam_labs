import random
import string
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Utils.compare_images import MonitorPicture

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.ru", "yahoo.com"]  # допустимые домены для email
letters = string.ascii_lowercase[:12]  # допустимые символы для случайно генерируемых строк


# Возвращает случайное доменное имя
def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def append_email_domain(func):
   def func_wrapper(name):
       return func(name) + get_random_domain(domains)
   return func_wrapper


# Возвращает случайный адрес email
@append_email_domain
def generate_random_email(length):
    return get_random_name(letters, length) + '@'


print(generate_random_email(5))


# Возвращает случайную строку заданной длины
def get_random_string(length):
    return get_random_name(letters, length)


# Возвращает возможное имя нового элемета в указанной папке
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

    return directory + "/" + str(curr_image_name + 1) + ".png"


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


# удаляет содержимое указанной папки
def clear_directory(directory):
    files = os.listdir(directory)
    images = filter(lambda x: x.endswith('.png'), files)

    for image in images:
        os.remove(directory + "/" + image)

    return 1
