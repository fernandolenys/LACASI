import math

import cv2
import numpy as np

image = cv2.imread("C:\\Users\\FERNANDO\\h.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows,cols = gray_image.shape
hist=np.zeros([256],dtype=int)

for i in range(rows):
      for j in range(cols):
            hist[gray_image[i][j]]+=1
mn=rows*cols
result=np.zeros([256],dtype=int)
for k in range(256):
    s=0
    for j in range(k+1):
        s+=hist[j]
    result[k]=round(s*255/mn)
for i in range(rows):
    for j in range(0,cols):
        gray_image[i][j]=result[gray_image[i][j]]


cv2.imshow("equalização de histograma", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
