import cv2
import numpy as np 
import imutils

img_color = cv2.imread('cat.jpg')
img_color = imutils.resize(img_color, width=500, height=500)
cv2.imshow("Cuttyyy", img_color)

height, width = img_color.shape[:2]

M = np.float32([[1, 0 ,100], [0, 1, 50]])

img_translation = cv2.warpAffine(img_color, M, (width, height))
cv2.imshow("translation", img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()