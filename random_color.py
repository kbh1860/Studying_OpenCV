import cv2
import numpy as np
from random import randint

#set width, height
width = 640
height = 480

#make the numpy array
#Argument = width, height, channel
img = np.zeros((width, height, 3), np.uint8)

#bring in h,w,channel
img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)

for y in range(img_h):
    for x in range(img_w):
        #change the color by random
        img.itemset(y, x, 0, randint(0, 255)) #b
        img.itemset(y, x, 1, randint(0, 255)) #g
        img.itemset(y, x, 2, randint(0, 255)) #r


while True:
    cv2.imshow("Random Color", img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()