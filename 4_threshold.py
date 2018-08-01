# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("Images/threshold.png", 0)

#Binarization Function. Threshold.
threshold, imgThreshold = cv2.threshold(img, 63, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold", imgThreshold)
cv2.waitKey(0)

#Flags
#cv2.THRESH_BINARY
#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV
# #cv2.THRESH_TOZERO_INV