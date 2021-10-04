import numpy as np
import cv2

img = cv2.imread('D:\Personal Work\Computer Vision\input images\crossword.jpg',0)


_,th_1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
th_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 12);
th_3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 12);


final_frame =cv2.hconcat([th_1,th_2,th_3])
cv2.imshow("Adaptive_Thresholding 1.Simple_threshold, 2.Ad_mean_c, 3.Ad_gaussian_c", final_frame)
cv2.waitKey()
cv2.destroyAllWindows()
