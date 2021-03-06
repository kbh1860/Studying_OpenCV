import cv2
import numpy as np

img = cv2.imread("./texture.png")
blur = cv2.bilateralFilter(img, 9, 75, 75)

merged = np.hstack((img, blur))

while True:
    cv2.imshow("merged", merged)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()