import cv2
import sys
import imutils

#CallBack Function
def on_trackbar(x):
    pass

img_color = cv2.imread("./half_dark.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_gray = imutils.resize(img_gray, width = 500, height = 500)

cv2.imshow("GrayScale", img_gray)

#Plus Window Trackbar
cv2.namedWindow("Binary")

#Create Trackbar
cv2.createTrackbar('threshold', "Binary", 0, 255, on_trackbar)

#Set Pos TrackBar
cv2.setTrackbarPos('threshold', "Binary", 127)

while True:
    #Get value of TrackbarPos
    thresh = cv2.getTrackbarPos('threshold', "Binary")

    #If pixel's value is less than threshold and pixel's color is white
    retval, img_binary = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY_INV)
    
    img_binary = imutils.resize(img_binary, width = 500, height = 500)

    cv2.imshow("Binary", img_binary)

    if(cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()