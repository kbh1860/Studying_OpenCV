import cv2

img_gray = cv2.imread('Image_Sample.jpg', cv2.IMREAD_GRAYSCALE)

# [start_y : end_y, start_x, end_x] -> ROI
img_sub1 = img_gray[20:20+170, 20:20+170]

cv2.line(img_sub1, (0,0 ), (100,100), 0, 10)

ret, img_sub1 = cv2.threshold(img_sub1, 127, 255, cv2.THRESH_BINARY)

#Not Equal
print(img_sub1.base is img_gray)

cv2.imshow("Img_Gray", img_gray)
cv2.imshow("Img_Sub1", img_sub1)

cv2.waitKey(0)
cv2.destroyAllWindows()