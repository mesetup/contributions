import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\Personal Work\Computer Vision\input images\cameraman.png',0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
g_blur =cv2.GaussianBlur(img,(5,5),0)
m_blur = cv2.medianBlur(img,5)
b_filter = cv2.bilateralFilter(img, 9 ,75 ,75)

images = [img,dst,blur,g_blur,m_blur,b_filter]
title = ["Original","2D_Convolution","Blur","Gaussian_blur","Median_blur","Bilateral_filter"]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
