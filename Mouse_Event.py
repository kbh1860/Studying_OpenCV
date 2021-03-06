import cv2
import numpy as np
import random

#Checking The Left Mouse Status
mouse_is_pressing = False
#Select The Draw Mode (Circle / Square)
drawing_mode = True

#Save The Value of Left Mouse Position
start_x, start_y = 1, -1

color = (255, 255, 255)

# Variable of Save The Image
img = np.zeros((512, 512, 3), np.uint8)

#If Mouse Event Trigger And Calling This Function
def mouse_callback(event, x, y, flags, param):

    global color, start_x, start_y, drawing_mode, mouse_is_pressing

    #If Moving The Mouse
    if event == cv2.EVENT_MOUSEMOVE:
        #If Pressing The Mouse And Moving
        if mouse_is_pressing == True:
            #Drawing Mode True == Drawing Square
            if drawing_mode == True:
                # Draw The Rectangle
                cv2.rectangle(img, (start_x, start_y), (x, y), color, -1)
            #Drawing Mode False == Drawing Circle
            else:
                cv2.circle(img, (start_x, start_y), max(abs(start_x - x), abs(start_y - y)) , color, -1)

    # If Click The Left Mouse
    elif event == cv2.EVENT_LBUTTONDOWN:
        #Random Color
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        mouse_is_pressing = True
        #Saving The Position 
        start_x, start_y = x, y

    #If Release one's Hand
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        #Drawing Rectangel Using Pressing Left Mouse And Release one's hand
        if drawing_mode == True:
            cv2.rectangle(img, (start_x, start_y), (x,y), color , -1)
        
        else:
            cv2.circle(img, (start_x, start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing_mode = 1 - drawing_mode

cv2.namedWindow("image")

cv2.setMouseCallback('image', mouse_callback)

while (True):
    cv2.imshow("image", img)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()