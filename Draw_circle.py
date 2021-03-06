import cv2
import numpy as np

width = 640
height = 480

img = np.zeros((width, height, 3), np.uint8)

cv2.circle(img,(320, 240), 10, (0,255,0), -1)
cv2.circle(img, (320, 420), 100, (0,0,255), 1)

cv2.imshow("circle", img)
cv2.waitKey(0)