import cv2
import numpy as np
from matplotlib import pyplot as plt

class image:
    def __init__(self):
        self.image = []
        self.filtered = []

    def load(self, filename):
        self.image = cv2.imread(filename)

    def medianfilter(self):
        self.filtered = cv2.medianBlur(self.image, 5)
        return

    def gaussianfilter(self):
        self.filtered = cv2.GaussianBlur(self.image, (5, 5), 0)
        return

    def display(self):
        plt.subplot(121), plt.imshow(self.image), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(self.filtered), plt.title('Filtered')
        plt.xticks([]), plt.yticks([])
        plt.show()

def main():
    img = image()
    img.load('noisy.jpg')
    img.medianfilter()
    img.display()
    img.gaussianfilter()
    img.display()
    # Median filter did a better job

if __name__ == "__main__":
    main()