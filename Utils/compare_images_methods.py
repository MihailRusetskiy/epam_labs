from PIL import Image


class CompareMethodFactory(object):
    def factory(type):
        if type == "HistoCompare":
            return HistoCompare()
        if type == "PixelCompare":
            return PixelCompare()
        if type == "XORCompare":
            return XORCompare()
        assert 0, "Bad car creation: " + type

    factory = staticmethod(factory)


class HistoCompare(CompareMethodFactory):
    def compare(self, im1, im2, mode="pct", alpha=.01):
        if im1.size == im2.size and im1.mode == im2.mode:
            h1 = im1.histogram()
            h2 = im2.histogram()
            SumIm1 = 0.0
            SumIm2 = 0.0
            diff = 0.0
            for i in range(len(h1)):
                SumIm1 += h1[i]
                SumIm2 += h2[i]
                diff += abs(h1[i] - h2[i])
            maxSum = max(SumIm1, SumIm2)
            if mode == "pct":
                return diff / (2 * maxSum)
            if diff > alpha * maxSum:
                return False
            return True
        return False


class PixelCompare(CompareMethodFactory):
    def compare(self, im1, im2, mode="pct", alpha=.01):
        if im1.size == im2.size and im1.mode == im2.mode:
            randPix = im1.getpixel((0, 0))
            maxSum = []
            diff = []
            for channel in range(len(randPix)):
                diff += [0.0]
                maxSum += [0.0]
            width = im1.size[0]
            height = im1.size[1]
            for i in range(width):
                for j in range(height):
                    pixel1 = im1.getpixel((i, j))
                    pixel2 = im2.getpixel((i, j))
                    for channel in range(len(randPix)):
                        maxSum[channel] += 255
                        diff[channel] += abs(pixel1[channel] - pixel2[channel])
            if mode == "pct":
                ret = ()
                for channel in range(len(randPix)):
                    ret += (diff[channel] / maxSum[channel],)
                return ret
            for channel in range(len(randPix)):
                if diff[channel] > alpha * maxSum[channel]:
                    return False
            return True
        return False


class XORCompare(CompareMethodFactory):
    def compare(self, im1, im2, mode="pct", alpha=.01):
        if im1.size == im2.size and im1.mode == im2.mode:
            XORCount = []
            randPix = im1.getpixel((0, 0))
            for channel in range(len(randPix)):
                XORCount += [0.0]
            width = im1.size[0]
            height = im1.size[1]
            imXOR = self.ImageXOR(im1, im2)
            maxSum = 0.0
            for i in range(width):
                for j in range(height):
                    pixel = imXOR.getpixel((i, j))
                    for channel in range(len(pixel)):
                        XORCount[channel] += pixel[channel]
                    maxSum += 255
            if mode == "pct":
                ret = ()
                for channel in range(len(randPix)):
                    ret += (XORCount[channel] / maxSum,)
                return ret
            for channel in range(len(randPix)):
                if XORCount[channel] > alpha * maxSum:
                    return False
            return True
        return False

    def ImageXOR(self, im1, im2):
        if im1.size == im2.size and im1.mode == im2.mode:
            width = im1.size[0]
            height = im2.size[1]
            ret = Image.new(im1.mode, im1.size)
            for i in range(width):
                for j in range(height):
                    pixel1 = im1.getpixel((i, j))
                    pixel2 = im2.getpixel((i, j))
                    putPix = ()
                    for channel in range(len(pixel1)):
                        putPix += (pixel1[channel] ^ pixel2[channel],)
                    ret.putpixel((i, j), putPix)
            return ret
        return False


def ImageCompare(im1, im2, mode="pct", alpha=.01):
    if im1.size == im2.size and im1.mode == im2.mode:

        compare_method = CompareMethodFactory.factory("HistoCompare")
        HistComp = compare_method.compare(im1, im2, "pct")

        compare_method = CompareMethodFactory.factory("PixelCompare")
        PixComp = compare_method.compare(im1, im2, "pct")

        compare_method = CompareMethodFactory.factory("XORCompare")
        XORComp = compare_method.compare(im1, im2, "pct")

        if mode == "pct":
            return HistComp, PixComp, XORComp
        if mode == "alpha":
            if HistComp > alpha:
                return False
            for pct in PixComp:
                if pct > alpha:
                    return False
            for pct in XORComp:
                if pct > alpha:
                    return False
            return True
    return False
