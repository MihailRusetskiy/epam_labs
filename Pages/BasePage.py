import logging


class BasePage(object):
    """Базовый класс для всех Page objects"""

    def __init__(self, driver):
        self.driver = driver
        # создание логгера
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # создание обработчиков для логгера
        # для сообщений уровня critical
        self.handler_critical = logging.FileHandler('../Output/Logs/critical.txt', 'w')
        self.handler_critical.setLevel(logging.WARNING)
        # для сообщеий уровня info
        self.handler_info = logging.StreamHandler()
        self.handler_info.setLevel(logging.INFO)

        # форматтеры
        self.formatter = logging.Formatter('%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler_critical.setFormatter(self.formatter)
        self.handler_info.setFormatter(self.formatter)

        # добавление обработчиков
        self.logger.addHandler(self.handler_info)
        self.logger.addHandler(self.handler_critical)
        