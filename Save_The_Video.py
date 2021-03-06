import cv2 as cv

cap = cv.VideoCapture(0)

if cap.isOpened() == False:
    print("Failed Open The Camera")
    exit(1)

ret, Img_Read = cap.read()

if ret == False:
    print("Faild Capture The Image")
    exit(1)

codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G') #Set The Codec Ex) MJPG, X264, WMV1... 

fps = 30.0 # Set The Video Frame

h,w = Img_Read.shape[:2] # Set The Video Size

writer = cv.VideoWriter("Output.avi", codec, fps, (w,h)) #Save The Video Obeject

if writer.isOpened() == False: #Failed To Make Object
    print("Can't Prepare The Video File")
    exit(1)

while(True):
    ret, Img_Read = cap.read()

    if ret == False:
        print("Failed Capture")
        break

    writer.write(Img_Read) #Save The Video

    cv.imshow('Color', Img_Read) # Show The Video

    Key = cv.waitKey(1)

    if Key == 27:
        break

cap.release()

writer.release() # End Of Save The Video

cv.destroyAllWindows()


