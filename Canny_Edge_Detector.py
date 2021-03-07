import cv2
import numpy as np
import imutils

img = cv2.imread("./apple.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = cv2.blur(img_gray, (3, 3))

img_canny = cv2.Canny(img_gray, 50, 150)

img_gray = imutils.resize(img_gray, width=500)
img_canny = imutils.resize(img_canny, width=500)
img = imutils.resize(img, width=500)

while True:
    cv2.imshow("Original", img)
    cv2.imshow("GrayScale", img_gray)
    cv2.imshow("Canny", img_canny)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()