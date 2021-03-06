import cv2
import sys

cap = cv2.VideoCapture(0)

if cap.isOpened() is False:
    print("Camera Error")
    sys.exit(1)

step = 1

while (True):
    
    ret, img_frame = cap.read()

    if (ret == False):
        print("Fail To Capture")
        break

    if(step == 2):
        img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)

    if(step == 3):
        img_frame = cv2.Canny(img_frame, 30, 90)

    cv2.imshow('result', img_frame)

    key = cv2.waitKey(1)

    if key == 27:
        break
    
    elif key == ord('1'):
        step = 1
    
    elif key == ord('2'):
        step = 2
    
    elif key == ord('3'):
        step = 3

cap.release()
cv2.destroyAllWindows()
    
