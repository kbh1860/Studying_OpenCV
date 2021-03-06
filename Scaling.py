import cv2
import imutils

img_color = cv2.imread('cat.jpg')
img_color = imutils.resize(img_color, width=500, height=500)

cv2.imshow("Cuttyyyy", img_color)

img_result = cv2.resize(img_color, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("x2 INTER_CUBIC", img_result)

height, width = img_color.shape[:2]

img_result = cv2.resize(img_color, (3 * width, 3 * height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("x3 INTER_LINEAR", img_result)

img_result = cv2.resize(img_color, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('x0.5 INTER_AREA', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.resize()