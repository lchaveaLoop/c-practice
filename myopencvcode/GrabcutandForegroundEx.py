import cv2
import numpy as np
import matplotlib.pyplot as pl

img=cv2.imread("foreground.jpg")
mask=np.zeros(img.shape[:2],np.uint8)

bgModel=np.zeros((1,65),np.float64)
fgModel=np.zeros((1,65),np.float64)

rect=(160,55,150,150)

cv2.grabCut(img,mask,rect,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype("uint8")
img=img*mask2[:,:,np.newaxis]

pl.imshow(img)
pl.colorbar()
pl.show()