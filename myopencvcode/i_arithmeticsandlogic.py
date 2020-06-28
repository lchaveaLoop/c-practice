import cv2
import numpy as np 

img1=cv2.imread("1.png")
img2=cv2.imread("3.png")

rows,clos,channels=img2.shape
roi=img1[0:rows,0:clos]

img2gray=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
ret,mask=cv2.threshold(img2gray,200,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst=cv2.add(img1_bg,img2_fg,mask=mask)

img1[0:rows,0:clos]=dst

cv2.imshow("mask",mask)
cv2.imshow("ret",img1)
cv2.imshow("dst",dst)
cv2.imshow("img_fg",img2_fg)
cv2.imshow("img1_bg",img1_bg)

# weight=cv2.addWeighted(img1,0.6,img2,0.3,0)

# cv2.imshow("weight",weight)
cv2.waitKey(0)
cv2.destroyAllWindows()