import cv2
import numpy as np
from matplotlib import pyplot as plt

class image:
    def __init__(self):
        self.image = []
        self.filtered = []
        self.height = 0
        self.width = 0

    def load(self, filename):
        self.image = cv2.imread(filename)

    def getdimension(self):
        dimension = self.image.shape
        self.height = dimension[0]
        self.width = dimension[1]
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

def inpaint(damaged, mask):
    pass

def main():
    mask = image()
    mask.load("damage_mask.bmp")
    mask.getdimension()

if __name__ == "__main__":
    main()