import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

background = 0

kernel_erode = np.ones((3, 3), np.uint8)
kernel_dilate = np.ones((3, 3), np.uint8)

time.sleep(3)
for i in range(60):
    _, background = cap.read()
    
background = cv2.flip(background, 1)

while True:

    ret, frame = cap.read()

    img = cv2.flip(frame, 1)
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,0])
    upper_red = np.array([200,250,200])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)

    mask = cv2.erode(mask, kernel_erode, 1)
    mask = cv2.dilate(mask, kernel_dilate, 1)

    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(background, background, mask = mask)   #background removed from original frame and  only red color parts remains(prev. background shows only in red region)
    fg = cv2.bitwise_and(img, img, mask = mask_inv)                 #foreground removed from cuurent frame i.e, red portion removed(blackout the red area from the frame)

    output = cv2.add(fg, bg)

   
    cv2.imshow("", output)
    

    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()




























    
    

    

