import numpy as np
import cv2

width = 640
height = 480
bpp = 3

img = np.zeros((width, height,bpp), np.uint8)

cv2.rectangle(img, (50,50), (450,450), (0,0,255),3)
cv2.rectangle(img, (150, 200), (250, 300), (0, 255, 0), -1)

cv2.imshow("rectangle", img)

cv2.waitKey(0)