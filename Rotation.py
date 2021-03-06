import cv2
import imutils

img_color = cv2.imread("./cat.jpg")

img_color = imutils.resize(img_color, width=500, height=500)

cv2.imshow("Cuttyyyyyyy", img_color)

height, width = img_color.shape[:2]

M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 45, 1)

print(type(height), width)

img_rotated = cv2.warpAffine(img_color, M, (width, height))

cv2.circle(img_rotated, (int(height / 2.0) , int(width / 2.0)), 3, (0, 255, 0), -1)

cv2.imshow("rotation", img_rotated)
cv2.waitKey(0)

cv2.destroyAllWindows()
