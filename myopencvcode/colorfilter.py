import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,0,60])
    upper_red=np.array([10,220,255])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    # kernel=np.ones((15,15),np.float32)/225
    # smoothed=cv2.filter2D(res,-1,kernel)
    # blur=cv2.GaussianBlur(res,(15,15),0)
    # median=cv2.medianBlur(res,15)
    # bilateral=cv2.bilateralFilter(res,15,75,75)
    cv2.imshow("frame",frame)
    # cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    # cv2.imshow("bilateral blurring",bilateral)
    # cv2.imshow("gaussian blurring",blur)
    # cv2.imshow("original",res)
    # cv2.imshow("averaging",smoothed)
    # cv2.imshow("median blurring",median)
    k=cv2.waitKey(5)&0xff
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()