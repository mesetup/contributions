import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

gray = cv.imread('D:\Personal Work\Computer Vision\input images\test_1.png', 0)
img = cv.cvtColor(gray, cv.cvtColor(gray,cv.color_BGR2GRAY))
kernel = np.ones((5,5), np.uint8)

erosion = cv.erode(img, kernel, iterations =1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
M_Gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
Top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
Black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

images = [erosion,dilation,opening,closing,M_Gradient,Top_hat,Black_hat]
title = ["Erosion","Dilation","Opening","Closing","M_Gradient","Top_hat","Black_hat"]

for i in range(7):
    plt.subplot(2, 4, i+1), plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
 
plt.show()     
     
