# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread("Images/coins.jpg", 0)

#Average Adaptive Threshold
adp1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#Average Adaptive Gaussiana
adp2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Original", img)
cv2.imshow("Adaptive Threshold - Average", adp1)
cv2.imshow("Adaptive Threshold - Gaussiana", adp2)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Limiar adaptativa baseada em Gaussiana
