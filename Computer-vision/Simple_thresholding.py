import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\Personal Work\Computer Vision\input images\gradient.jpg',0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

_,th_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_,th_2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_,th_3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_,th_4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_,th_5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

images = [th_1,th_2,th_3,th_4,th_5]
title = ["Binary","Binary_inverted","Trunced","To_zero","To_zero_inv"]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()