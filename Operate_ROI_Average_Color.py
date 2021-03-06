import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    ret, img_color = cap.read()
    img_result = img_color.copy()

    height, width = img_color.shape[:2]

    center_x = int(width * 0.5)
    center_y = int(height * 0.5)

    cv2.rectangle(img_result, (center_x - 100, center_y - 100), (center_x + 100, center_y + 100), (0, 0, 255), 3)

    img_roi = img_color[center_y - 100 : center_y + 100, center_x - 100 : center_x + 100]

    m = cv2.mean(img_roi)

    img_mean = np.zeros(img_roi.shape, dtype=np.uint8)
    img_mean[:]  = (m[0], m[1], m[2])

    cv2.imshow('mean', img_mean)
    cv2.imshow('color', img_result)
    cv2.imshow("roi", img_roi)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()