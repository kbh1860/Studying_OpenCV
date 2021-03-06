import cv2
import numpy as np 

Img_Color = cv2.imread('Image_Sample.jpg', cv2.IMREAD_COLOR)

# 이미지의 높이와 너비를 가져온다.
height, width = Img_Color.shape[:2]

#Gray Scale 이미지를 저장할 넘파이 배열 생성
img_gray = np.zeros((height, width), np.uint8)

#for 문을 돌리면서 x,y에 있는 픽셀을 하나씩 접근
for y in range(0, height):
    for x in range(0, width):
        
        #컬러 이미지 x,y에 있는 픽셀의 bgr채널을 읽는다.
        #Argument = (First_Position, Second_Position, Number, RGB)
        b = Img_Color.item(y, x, 0)
        g = Img_Color.item(y, x ,1)
        r = Img_Color.item(y, x, 2)

        #x, y 위치의 픽셀에 그레이 스케일 값 저장
        gray = int((r+g+b) / 3.0)

        img_gray.itemset(y, x, gray)

#컬러 이미지 변환
img_result = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# 150부터 201 / 200부터 251까지 초록색 픽셀로 변환
for y in range(150, 201):
    for x in range(200, 251):
        img_result.itemset(y, x, 0, 0)
        img_result.itemset(y, x, 1, 255)
        img_result.itemset(y, x, 2, 0)

cv2.imshow("color", Img_Color)
cv2.imshow("result", img_result)

cv2.waitKey(0)

cv2.destroyAllWindows()