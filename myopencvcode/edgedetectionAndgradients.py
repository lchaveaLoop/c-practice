import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edge=cv2.Canny(frame,50,50)

    cv2.imshow("frame",frame)
    # cv2.imshow("laplacian",laplacian)
    # cv2.imshow("sobely",sobely)
    # cv2.imshow("sobelx",sobelx)
    cv2.imshow("edge",edge)
    
    k=cv2.waitKey(5)&0xff
    if k==27:
        break


cv2.destroyAllWindows()
cap.release()