import cv2
import numpy
import matplotlib.pyplot as plot

img=cv2.imread('watch1.jpeg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plot.imshow(img,cmap='gray',interpolation='bicubic')
# plot.show()

plot.plot([50,100],[70,100],'c',linewidth=8)
plot.show()
# cv2.imwrite("watchgray.png",img)