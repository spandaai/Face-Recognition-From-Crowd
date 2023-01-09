# upsample.py
import cv2
import numpy as np
import joblib


class Upsample():
    def set_image(self, img, scale):
        self.img = cv2.imread(img)
        self.og_size = self.img.shape
        self.upsampled_size = (
            int(self.og_size[1] * scale), int(self.og_size[0] * scale))

    def interpolation(self, method='bicubic'):
        if method == 'nearest':
            method = cv2.INTER_NEAREST
        elif method == 'bilinear':
            method = cv2.INTER_LINEAR
        elif method == 'bicubic':
            method = cv2.INTER_CUBIC
        elif method == 'lanczos':
            method = cv2.INTER_LANCZOS4
        else:
            raise Exception('Invalid interpolation method')
        self.img = cv2.resize(
            self.img, self.upsampled_size, interpolation=method)

    def super_resolution_gan(self, method):
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        if method == 'espcn':
            path = '../weights/ESPCN_x2.pb'
        else:
            raise Exception('Invalid method')
        sr.readModel(path)
        sr.setModel(method, 2)
        self.img = sr.upsample(self.img)

    def denoising(self):
        self.image = cv2.fastNlMeansDenoisingColored(
            self.img, None, 10, 10, 7, 21)

    def sharpening(self):
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        self.img = cv2.filter2D(self.img, -1, kernel)

    def sharpening_mask(self):
        blue, green, red = cv2.split(self.img)
        sharpened_blue = cv2.addWeighted(
            blue, 1.5, cv2.GaussianBlur(blue, (0, 0), 3), -0.5, 0)
        sharpened_green = cv2.addWeighted(
            green, 1.5, cv2.GaussianBlur(green, (0, 0), 3), -0.5, 0)
        sharpened_red = cv2.addWeighted(
            red, 1.5, cv2.GaussianBlur(red, (0, 0), 3), -0.5, 0)
        self.img = cv2.merge((sharpened_blue, sharpened_green, sharpened_red))

    def save_image(self, name):
        cv2.imwrite(name, self.img)


if __name__ == '__main__':
    upsample = Upsample()
    upsample.set_image('../test/michael-jackson-bad-low-res-58.jpg', 0.5)

    upsample.denoising()
    upsample.save_image('../test/1_denoised.jpg')
    upsample.sharpening_mask()
    upsample.save_image('../test/1_sharpened.jpg')

    upsample.super_resolution_gan('espcn')
    upsample.save_image('../test/1_upsampled.jpg')

    upsample.interpolation()
    upsample.save_image('../test/1_1.jpg')
