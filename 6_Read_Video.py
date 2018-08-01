# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
   status, image =  cap.read()
   cv2.imshow("Capture", image)

   k = cv2.waitKey(1) & 0xFF
   if k == 27:
       break

cv2.destroyAllWindows()
cap.release()