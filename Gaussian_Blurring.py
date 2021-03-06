import cv2
import numpy as np

img = cv2.imread("./test.png")
Gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.GaussianBlur()
ave_blur = cv2.blur(img, (5,5))

merged = np.hstack((img, Gaussian_blur, ave_blur))

while True:
    cv2.imshow("Merged", merged)

    key = cv2.waitKey(0)

    if key == 27:
        break

cv2.destroyAllWindows()