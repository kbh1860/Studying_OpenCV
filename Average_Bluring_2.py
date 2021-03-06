import cv2

img = cv2.imread("./test.png")
img_blur = cv2.blur(img, (5,5))


while True:
    cv2.imshow("Original", img)
    cv2.imshow("Blur", img_blur)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()