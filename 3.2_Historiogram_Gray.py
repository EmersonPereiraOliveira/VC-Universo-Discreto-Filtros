# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images/soccer.jpg", 0)

#Plot in Gray Scale
    #.ravel Tranform the Vector Multidensional in a Vector  One-dimensional
plt.hist(img.ravel(), 256, [0, 256])

cv2.imshow("Imagem original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()