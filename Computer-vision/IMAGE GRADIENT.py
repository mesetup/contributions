import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('/home/ritik/Documents/input images/crossword.jpg',0)
image = cv.cvtColor(image,cv.COLOR_BGR2RGB)

lap = cv.Laplacian(image,cv.CV_64F,ksize=1)
lap = np.uint8(np.absolute(lap))

SobelX = cv.Sobel(image,cv.CV_64F,1,0)
SobelY = cv.Sobel(image,cv.CV_64F,0,1)

SobelX = np.uint8(np.absolute(SobelX))
SobelY = np.uint8(np.absolute(SobelY))

Sobelcombined = cv.bitwise_or(SobelX,SobelY)

images=[image, lap ,SobelX, SobelY, Sobelcombined]
title =["Original", "Laplacian" , "SobelX","SobelY", "SobelCombined"]

for i in range(6):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()

