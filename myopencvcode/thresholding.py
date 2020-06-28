import cv2
import numpy 

img = cv2.imread("4.jpeg")
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2=cv2.threshold(grayimg,12,255,cv2.THRESH_BINARY) 
gaus=cv2.adaptiveThreshold(grayimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

graycimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("orginal",img)
cv2.imshow("threshold2",threshold2)
cv2.imshow("gaus",gaus)
cv2.imshow("threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()