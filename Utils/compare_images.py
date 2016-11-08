from Utils.compare_images_methods import *
from PIL import Image


def MonitorPicture(file1, file2, method="all", tolerance=.01):
    image = Image.open(file1)
    image2 = Image.open(file2)

    if method == "all":
        if ImageCompare(image, image2, "alpha", tolerance) == False:
            res = 1
        else: res = 0

    elif method == "hist":
        compare_method = CompareMethodFactory.factory("HistoCompare")
        if compare_method.compare(image, image2, "pct") == False:
            res = 1
        else: res = 0

    elif method == "pix":
        compare_method = CompareMethodFactory.factory("PixelCompare")
        if compare_method.compare(image, image2, "pct") == False:
            res = 1
        else: res = 0

    elif method == "xor":
        compare_method = CompareMethodFactory.factory("XORCompare")
        if compare_method.compare(image, image2, "pct") == False:
            res = 1
        else: res = 0
    else:
        res = 0

    return res
