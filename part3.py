import cv2
from matplotlib import pyplot as plt

class image:
    def __init__(self, filename):
        self.image = cv2.imread(filename)
        self.filtered = []
        self.height = 0
        self.width = 0
        # Use the switch to identify if self.gaussianfilter() has been called before
        self.switch = 0
        self.getdimension()

    # Get image dimension (Height and Width)
    def getdimension(self):
        dimension = self.image.shape
        self.height = dimension[0]
        self.width = dimension[1]
        return

    # Apply gaussianfilter
    def gaussianfilter(self):
        if self.switch == 0:
            self.filtered = cv2.GaussianBlur(self.image, (5, 5), 0)
            self.switch = 1
        else:
            self.filtered = cv2.GaussianBlur(self.filtered, (5, 5), 0)
        return

    def display(self):
        plt.subplot(121), plt.imshow(self.image), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(self.filtered), plt.title('Filtered')
        plt.xticks([]), plt.yticks([])
        plt.show()


def inpaint(damaged, mask):
    damaged.gaussianfilter()
    for i in range(0, damaged.height):
        for j in range(0, damaged.width):
            if mask.image[i][j][0] != 0:
                damaged.filtered[i][j] = damaged.image[i][j]
    return


def multi_inpaint(damaged, mask, iter):
    for i in range(0, iter):
        inpaint(damaged, mask)
    return


def main():
    mask = image("damage_mask.bmp")
    damaged = image("damaged_cameraman.bmp")
    # Modify the iteration time to achieve better result.
    multi_inpaint(damaged, mask, 25)
    damaged.display()

if __name__ == "__main__":
    main()