import cv2
import numpy as np

img = cv2.imread("./median.png")
median = cv2.medianBlur(img, 5)

merged = np.hstack((img, median))

while True:
    cv2.imshow("Merged", merged)

    key = cv2.waitKey(0)

    if key == 27:
        break

cv2.destroyAllWindows()
