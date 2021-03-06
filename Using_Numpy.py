import cv2

img_gray = cv2.imread("Image_Sample.jpg", cv2.IMREAD_GRAYSCALE)

#Substitute

img_copyed1 = img_gray

#Equal
print(id(img_gray), id(img_copyed1))

#Draw Line
cv2.line(img_gray, (0, 0), (100, 100), 0, 10)

#Making Binary
ret, img_copyed1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

print(id(img_gray), id(img_copyed1))


while True:
    cv2.imshow("Img_Gray", img_gray)
    cv2.imshow("Img_Copyed", img_copyed1)
    cv2.waitKey(0)

cv2.destroyAllWindows()