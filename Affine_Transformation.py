import numpy as np
import cv2

#Mouse Position
point_list = []

#CallBack Function
def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        print(x, y)

        #Store The Position
        point_list.append((x,y))
        cv2.circle(img_color, (x,y), 3, (0, 0, 255), -1)

#Register The CallBack Function
cv2.namedWindow('source')
cv2.setMouseCallback('source', mouse_callback)

img_color = cv2.imread("./test.png")

while True:
    cv2.imshow('source', img_color)

    if cv2.waitKey(1) == 32:
        break

height, weight = img_color.shape[:2]

#Original Position || Original Position + 100
pts1 = np.float32([point_list[0], point_list[1], point_list[2]])
pts2 = np.float32([point_list[0], point_list[1], point_list[2]])
pts2[1][1] += 100

# for i in range(3):
#     print(point_list[i])

#Make The Transformation
M = cv2.getAffineTransform(pts1, pts2)

#Affine
img_result = cv2.warpAffine(img_color, M, (weight, height))

cv2.imshow('result', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

