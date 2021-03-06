import cv2
import imutils
import numpy as np 
import time

# Select The Threshold
alpha = 0.0
beta = 1.0

while alpha <= 1.0:

    img1 = cv2.imread('./cat.jpg', cv2.IMREAD_COLOR)
    img2 = cv2.imread('./beach.jpg', cv2.IMREAD_COLOR)

    #If You want use cv2.addWeighted(), You should read the same size picture
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    dst = cv2.addWeighted(img1, alpha, img2_resized, beta, 0)

    #print Threshold
    print(alpha, " ", beta)

    dst = imutils.resize(dst, width=500, height=500)
    cv2.imshow("dst", dst)
    
    key = cv2.waitKey(1)

    if key == 27:
        break
    
    # Up & Down Threshold
    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)
    
    time.sleep(0.2)

cv2.destroyAllWindows()