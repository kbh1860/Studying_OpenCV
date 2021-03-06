import cv2 

Img_Color = cv2.imread("Image_Sample.jpg", cv2.IMREAD_COLOR)

if Img_Color is None:
    print("Failed To Load Image")
    exit(1)

cv2.namedWindow("Color")

cv2.imshow('Color', Img_Color)

cv2.waitKey(0)

Img_Gray = cv2.cvtColor(Img_Color, cv2.COLOR_BGR2GRAY) #Change The Color To Gray
#First Parameter = RGB Color Picture Src
#Second Parameter = What You Want For Change Color Option

cv2.imshow("GrayImage", Img_Gray)

cv2.imwrite("Gray_Image_Sample.jpg", Img_Gray) #Save The Image Function
#First Parameter = The Name for Save Image File
#Second Parameter = File Src

cv2.waitKey(0)

cv2.destroyAllWindows()
