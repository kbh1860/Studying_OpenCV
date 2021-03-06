import cv2
import numpy as np
import imutils

img_logo = cv2.imread('./logo.png', cv2.IMREAD_COLOR)
img_background = cv2.imread('./background.png', cv2.IMREAD_COLOR)

# LogoImage = GrayScale -> Binarization
img_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
ret, img_mask = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

# Flip the img_mask
img_mask_inv = cv2.bitwise_not(img_mask)

# Cut the size of logo image in img_background
# The position of insert the logo image
height, width = img_logo.shape[:2]
img_roi = img_background[0:height, 0:width]

# Delect the background img in logo img Using Binarization
img1 = cv2.bitwise_and(img_logo, img_logo, mask=img_mask_inv)
# Delect the position of logo image in background
img2 = cv2.bitwise_and(img_roi, img_roi,mask=img_mask)

# add image
dst = cv2.add(img1, img2)

# copy the img to background img
img_background[0:height, 0:width] = dst

while True:
    cv2.imshow("Hello", img_background)
    cv2.imshow("img_logo_binarization", img_mask)
    cv2.imshow("img_mask_flip", img_mask_inv)
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow('dst', dst)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()