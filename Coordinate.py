import cv2
import numpy as np


width = 640
height = 400


img = np.zeros((height, width, 3), np.uint8)


img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)

cv2.circle(img, (100, 300), 10, (0, 255, 255), -1)

while True:
    cv2.imshow('circle', img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
