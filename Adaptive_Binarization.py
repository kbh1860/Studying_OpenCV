import cv2
import sys
import imutils

img_color = cv2.imread("./half_dark.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("Failed")
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

img_binary = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5 , 4)

img_gray = imutils.resize(img_gray, height = 500, width = 500)
img_binary = imutils.resize(img_binary, height = 500, width = 500)

while True:
    cv2.imshow("GrayScale", img_gray)
    cv2.imshow("Binary", img_binary)

    if(cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()