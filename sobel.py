import math

import cv2
import numpy as np

image = cv2.imread("C:\\Users\\FERNANDO\\test2.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("opencv ex", image)

print ('Gray shape:', gray_image.shape)
rows,cols = gray_image.shape


maskh=[[-1,0,1],
      [-2, 0,2],
      [-1,0,1]]
maskv=[[1,2,1],
      [0, 0,0],
      [-1,-2,-1]]
imageh=np.zeros((rows,cols))
imagev=np.zeros((rows,cols))

for i in range(1,rows-1):
      for j in range(1,cols-1):
        s=0
        for m in range(3):
            for n in range(3):
                p = gray_image[i-1+m, j-1+n]
                s+=p*maskh[m][n]
        imageh[i][j]=s/9

for i in range(1,rows-1):
      for j in range(1,cols-1):
        s=0
        for m in range(3):
            for n in range(3):
                p = gray_image[i-1+m, j-1+n]
                s+=p*maskv[m][n]
        imagev[i][j]=s/9

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        gray_image[i][j]=(imageh[i][j]**2 + imagev[i][j]**2)**1/2
cv2.imshow("sobel", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
