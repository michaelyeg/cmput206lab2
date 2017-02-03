import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')

kernel = -np.ones((3,3),np.float32)
# Set center pixel value as 8
kernel[1][1] = 8
# Set pixel value as -1 elsewhere
dst = cv2.filter2D(img,-1,kernel)

combined = cv2.addWeighted(img, 0.5, dst, 0.5, 0.0)

plt.subplot(131), plt.imshow(img), plt.title('Before')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(dst), plt.title('After')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(combined),plt.title('Combined')
plt.xticks([]), plt.yticks([])
plt.show()

# Observe some edge enhancements, darkened image