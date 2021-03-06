import cv2
import numpy as np

img = cv2.imread("./test.png")
kernel = np.ones((5,5), np.float32) / 5 ** 2
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()