from selenium import webdriver


class Singleton(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            cls.driver = webdriver.Chrome('/usr/bin/chromedriver')
        else:
            i = cls.instance
        return i

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


class DriverInstance(Singleton):
    @staticmethod
    def get_instance():
        return Singleton().instance.driver
