from PIL import Image


def get_element_screen(driver, element, filename):

    location = element.location
    size = element.size
    driver.save_screenshot(filename) # saves screenshot of entire page

    im = Image.open(filename) # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save(filename) # saves new cropped image
