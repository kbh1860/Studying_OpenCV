import cv2 #필요한 openCV 패키지를 임포트한다.

Img_Color = cv2.imread("Image_Sample.jpg", cv2.IMREAD_COLOR) 
#First Parameter = File Name
#Second Parameter = Show File Option

if Img_Color is None:
    print("이미지를 불러올 수 없습니다.")
    exit(1)

cv2.namedWindow("Sample_Image")  #Make Image Window
#First Parameter = Window Caption Name
#Second Parameter = Image Sizing
cv2.imshow('Sample_Image', Img_Color) 
#First Parameter = Windows Name
#Second Parameter = File Name 

cv2.waitKey(0)

cv2.destroyAllWindows()
