import cv2
import numpy as np
import imutils

img = cv2.imread("./test.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

# img_sobel_x = imutils.resize(img_sobel_x, width=300)
# img = imutils.resize(img, width=300)

# merged = np.hstack((img, img_sobel_x))

while True:
    cv2.imshow("Original", img)
    cv2.imshow("Sobel", img_sobel_x)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
