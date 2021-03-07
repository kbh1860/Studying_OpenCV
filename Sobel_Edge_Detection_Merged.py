import cv2
import numpy as np
import imutils

img = cv2.imread("./test.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

img_sobel_x = cv2.convertScaleAbs(img_sobel_x)
img_sobel_y = cv2.convertScaleAbs(img_sobel_y)

img_sobel = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0)

# img_sobel_x = imutils.resize(img_sobel_x, width=300)
# img = imutils.resize(img, width=300)

# merged = np.hstack((img, img_sobel_x))

while True:
    cv2.imshow("Merged", img_sobel)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
