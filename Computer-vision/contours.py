import cv2
import numpy as np
import  imutils

img = cv2.imread('D:\Personal Work\Computer Vision\input images\plate.jpg')
img = imutils.resize(img, width=500)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2 - Bilateral Filter", gray)
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("4 - Canny Edges", edged)
(new, cnts ) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts= sorted(cnts,  cv2.contourArea)[:30]

ret, threshold = cv2.threshold(gray, 127, 255 , 0)
edge = cv2.Canny(threshold,100,200)
contours, hierarchy = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1, (0,255,0), 3)

cv2.imshow("IMAGE", img)
cv2.waitKey()
cv2.destroyWindow()