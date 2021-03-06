import cv2
import sys
import imutils

img_color = cv2.imread("./apple.png", cv2.IMREAD_COLOR)

if img_color is None:
    print("Failed")
    sys.exit(1)

#GrayScale Change
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#Threshold == 127
#Binary Flag == THRESH_BINARY
#If Pixel's value is less than 127 and Pixel's value =  0
#Else Pixel's Value = 1
 
retval, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

#Resize
img_color = imutils.resize(img_color, height = 500, width = 500)
img_gray = imutils.resize(img_gray, height = 500, width = 500)
img_binary = imutils.resize(img_binary, height = 500 , width = 500)

while True:
    cv2.imshow("Original", img_color)
    cv2.imshow("Grayscale", img_gray)
    cv2.imshow("Binary", img_binary)
    cv2.waitKey(0)

cv2.destroyAllWindows()