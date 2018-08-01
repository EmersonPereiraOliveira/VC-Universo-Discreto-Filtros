# -*- coding: utf-8 -*-
import cv2

#Load Image
img = cv2.imread("Images/girls.jpg", 0)

cv2.imshow("Image", img)

#Wait for key
cv2.waitKey(0)

#Destroy All Windows
cv2.destroyAllWindows()

#Save Image in GrayScale
cv2.imwrite("Images/girls_gray.jpg", img)