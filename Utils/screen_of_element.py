from PIL import Image


""" скриншот элемента страницы
аргументы:
driver    экземпляр webdriver
element   ссылка на элемет на странице
filename  полняй путь куда сохранять изображение"""

def get_element_screen(driver, element, filename):

    location = element.location
    size = element.size
    driver.save_screenshot(filename) # сохраняем криншот страницы

    im = Image.open(filename) # с помощью PIL загружаем в памяь

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom)) # обрезаем картинку
    im.save(filename) # сохраняем обрезанную картинку
