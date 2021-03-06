import cv2

IMG = cv2.imread('Image_Sample.jpg') # IMG Read 

if IMG is None: #Can't load
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)


cv2.imshow('IMG', IMG) #Show The Image

cv2.waitKey(0) #If Press 'Q'
cv2.destroyAllWindows() #Quit All Windows