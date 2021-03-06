import cv2

#Check The Pressing Status Of Mouse
mouse_is_pressing = False
#Reset The Value
start_x, end_x, start_y, end_y = 0,0,0,0
#Check The Event Status
step = 0
temp = 0
#Swap The Position
def swap(v1, v2):
    global temp
    temp = v1
    v1 = v2
    v2 = temp

#Press The Left Button Of Mouse == Start Position Of ROI
#Release The Left Button Of Mouse == End Position Of ROI
#If Moving The Mouse And Draw Rectangle By ROI Region
def Mouse_Callback(event, x, y, flags, param):
    global step, start_x, end_x, start_y, end_y, mouse_is_pressing

    #Press The Left Button
    if event == cv2.EVENT_LBUTTONDOWN:
        step = 1
        mouse_is_pressing = True
        start_x = x
        start_y = y
    
    #Moving The Mouse
    elif event == cv2.EVENT_MOUSEMOVE:
        #If Pressing The Mouse
        if mouse_is_pressing:
            end_x = x
            end_y = y
            step = 2
            
    #Release The Left Button
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        end_x = x
        end_y = y

        step = 3

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Cant Open The Camera")
    exit(-1)

cv2.namedWindow("Color")
#cv2.setMouseCallback(windowName, onMouse, param = None)
#windowName = Dispose Of The Mouse Event in Window
#onMouse = Call Back Function
#param = Data of CallBack Function's Argument
cv2.setMouseCallback("Color", Mouse_Callback)

while True:

    ret, img_color = cap.read()

    if ret == False:
        print("Cant Load The Camera")
        break

    #Press The Left Button
    if step == 1:
        cv2.circle(img_color , (start_x, start_y), 10, (0, 255, 0), -1)

    #Moving The Mouse
    elif step == 2:
        cv2.rectangle(img_color, (start_x, start_y), (end_x, end_y), (0, 255, 0), 3)

    #Release Of The Mouse
    elif step == 3:
        #If Start X Position Is Bigger Than End X
        if start_x > end_x:

            swap(start_x, end_x)
            swap(start_y, end_y)

        
        ROI = img_color[start_y : end_y, start_x : end_x]

        ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
        ROI = cv2.Canny(ROI, 150, 50)
        ROI = cv2.cvtColor(ROI, cv2.COLOR_GRAY2BGR)

        img_color[start_y : end_y, start_x : end_x] = ROI

    cv2.imshow("Color", img_color)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()