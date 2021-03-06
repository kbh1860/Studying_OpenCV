import cv2

img_color = cv2.imread('./Image_Sample.jpg' , cv2.IMREAD_COLOR )

height, width = img_color.shape[:2]

center_x, center_y = int(width * 0.5), int(height * 0.5)

# Set the ROI with center Position
# If you use copy method, You will not edit original image
img_roi = img_color[center_y - 100 : center_y + 100, center_x - 100 : center_x + 100].copy()

img_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(img_gray, 100, 300)

# Translate Color image To Copy original imge
img_edge1 = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)

#Copy To Original Image
img_color[center_y- 100 : center_y + 100, center_x - 100 : center_x + 100]= img_edge1

while True:
    cv2.imshow("COLOR", img_color)
    cv2.imshow("ROI", img_roi)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()