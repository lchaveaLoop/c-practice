import numpy as np
import cv2 
img = cv2.imread("watch1.jpeg",cv2.IMREAD_COLOR)

# cv2.line(img,(0,0),(150,150),(0,0,2),15)
# cv2.rectangle(img,(12,15),(120,110),(0,255,255),5)
# cv2.circle(img,(90,50),60,(255,0,0),2)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts=pts.reshape((-1,2,2))
cv2.polylines(img,[pts],True,(0,255,255),5)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OPENCV LEARNING!",(0,130),font,0.8,(20,255,255),2,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()