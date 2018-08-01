# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images/soccer.jpg", 1)

#Creare a list
cor = ('b','g','r')

#Return Position and Value
for i, col in enumerate(cor):
    #Generate Histogram
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    #Plot Histogram
    plt.plot(histr, color = col)
    plt.xlim([0, 256])

cv2.imshow("Original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()