import cv2

img_gray = cv2.imread("Image_Sample.jpg", cv2.IMREAD_GRAYSCALE)

# Numpy Copy
img_copyed1 = img_gray.copy()

#Not Equal
print(id(img_copyed1), id(img_gray))

cv2.line(img_gray, (0,0), (100,100), 0, 10)

ret, img_copyed1 = cv2.threshold(img_copyed1, 127, 255, cv2.THRESH_BINARY)

#Not Equal
print(id(img_gray), id(img_copyed1))

cv2.imshow("Img_Gray", img_gray)
cv2.imshow("Img_Copyed", img_copyed1)

cv2.waitKey(0)
cv2.destroyAllWindows()