import cv2
import numpy as np

img = cv2.imread('D:\Personal Work\Computer Vision\input images\cameraman.png')
#copying the image to another variable
layer = img.copy()

#creating gaussian pyramids in array i.e in a list
gp = [layer]

#looping the layer
for i in range(6): #for five image pyramids
    layer = cv2.pyrDown(layer) # here this fumnction is used to reduce the resolution of our test image
    gp.append(layer) #here the result will add to our list
    cv2.imshow(str(i),layer)

#laplacian pyramid
layer = gp[5]  #index 5 is used i.e last image
cv2.imshow("upper_level_gaussian_pyramid",layer)

#creating laplacian pyramids in array i.e in a list
lp = [layer]

#looping the layer
for i in range(5, 0 ,-1):
    gaussian_extendent = cv2.pyrUp(gp[i])
    #extendent version of its upper layer in gaussian pyramid
    laplacian = cv2.subtract(gp[i-1],gaussian_extendent)
    cv2.imshow(str(i), laplacian)

cv2.waitKey()
cv2.destroyAllWindows()


