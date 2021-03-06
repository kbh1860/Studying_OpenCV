import cv2
import numpy as np

#Mouse Position Store this Variable
src = np.zeros([4, 2], dtype=np.float32)
idx = 0

#Call Back Function
def mouse_callback(event, x, y, flags, param):
    global point_list, idx

    #Store The Mouse Position
    if event == cv2.EVENT_LBUTTONDOWN:
        src[idx] = (x, y)
        idx = idx + 1

        print(x, y)
        cv2.circle(img_color, (x, y), 10, (0, 0, 255), -1)

#Register The Mouse CallBack Function
cv2.namedWindow('original')
cv2.setMouseCallback('original', mouse_callback)

#Reead The Image
img_color = cv2.imread("./Perspective.jpg")
img_original = img_color.copy()

#Set The Position
while True:
    cv2.imshow('original', img_color)

    height, width = img_color.shape[:2]

    if cv2.waitKey(1) == 32:
        break

#2 Dimension Position
dst = np.float32([[0,0], [width, 0], [0, height], [width, height]])

#Perspective Transformation
M = cv2.getPerspectiveTransform(src, dst)

img_result = cv2.warpPerspective(img_original, M, (width, height))

cv2.imshow('result1', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()