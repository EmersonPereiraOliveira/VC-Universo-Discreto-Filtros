# -*- coding: utf-8 -*-
import numpy as np
import cv2

#Read Image
imgSoccer = cv2.imread("Images/soccer.jpg", 1)

#Return Width, Height and Number of Color Channels
print(imgSoccer.shape)

#Show Pixel in the Position (BGR)
print(imgSoccer.item(0,0,0))
print(imgSoccer.item(0,0,1))
print(imgSoccer.item(0,0,2))

#Set Pixel Color (BGR)
imgSoccer.itemset((0, 0, 0), 0)
imgSoccer.itemset((0, 0, 1), 0)
imgSoccer.itemset((0, 0, 2), 255)

#Show Image
cv2.imshow("Show Soccer", imgSoccer)
cv2.waitKey(0)

#Crop Pixels Set
ball = imgSoccer[180:250, 250:315]

#Save Cropped Ball
cv2.imwrite("Images/ball_cropped.jpg", ball)
cv2.waitKey(0)