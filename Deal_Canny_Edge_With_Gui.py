import cv2

# If Mediate THe TrackBar, CallBack Function
# You Can Insert openCV Function In here
# Dummy Function
def on_trackbar(x):
    pass

cv2.namedWindow('Canny')

# openCV Provide GUI Function Of TrackerBar
# Argument = 1. Trackbar's Name, 2. Window's Name, 3.Trackbar's Minimum, 4. Trackbar's Maximum, 5. CallBack Function
cv2.createTrackbar('Low Threshold', 'Canny', 0, 1000, on_trackbar)
cv2.createTrackbar('High Threshold', 'Canny', 0, 1000, on_trackbar)

# Set Trackbar's Initial value
# draw close To Trackbar's Name, Window's Name
cv2.setTrackbarPos('Low Threshold', 'Canny', 50)
cv2.setTrackbarPos('High Threshold', 'Canny', 150)

# Input of Canny Edge is only GrayScale
img_gray = cv2.imread("Image_Sample.jpg", cv2.IMREAD_GRAYSCALE)


while (True):
    # Bring The Now Trackbar's Position
    low = cv2.getTrackbarPos("Low Threshold", 'Canny')
    high = cv2.getTrackbarPos("High Threshold", "Canny")

    # Modulate By Trackbar's Value
    img_canny = cv2.Canny(img_gray, low, high)

    # Show The Image
    cv2.imshow('Canny', img_canny)

    if (cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()