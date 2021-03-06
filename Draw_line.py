import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

 
cv.line(img, (width, 0), (0, height), (0, 255, 0), 3)
cv.line(img, (0, 0), (width, height), (0, 0, 255), 3) 
print(width - 1)

cv.imshow("result", img)
cv.waitKey(0);