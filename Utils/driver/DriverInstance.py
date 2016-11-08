import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utils.proxy import create_proxyauth_extension


class Singleton(object):
    instance = None  # переменная для хранения экземпляра webdriver

    def __new__(cls):
        if cls.instance is None:  # если экземпляра webdriver не существует
            i = object.__new__(cls)
            cls.instance = i
            cls.driver = webdriver.Chrome('/usr/bin/chromedriver')  # инициализируем новый экземпляр
        else:  # если экземпляр webdriver существует
            i = cls.instance  # возвращаем ссылку на него
        return i


"""
Возвращает экземпляр webdriver, реализуя паттерн singleton
"""
class DriverInstance(Singleton):
    @staticmethod
    def get_instance():
        return Singleton().instance.driver

