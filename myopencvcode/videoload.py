import numpy as np
import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'mpeg')
out=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while(1):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    if cv2.waitKey(1)&0xff==ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
        
