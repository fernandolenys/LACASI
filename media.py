import math

import cv2
import numpy as np

#image = cv2.imread("C:\\Users\\FERNANDO\\test.jpg")
image = cv2.imread("C:\\Users\\FERNANDO\\test2.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("opencv ex", image)

print ('Gray shape:', gray_image.shape)
rows,cols = gray_image.shape

mask=np.zeros((3,3))
mask=[[1,1,1],
      [1,1,1],
      [1,1,1]]

for i in range(1,rows-1):
      for j in range(1,cols-1):
        s=0
        #print (i,j,p)
        for m in range(3):
            for n in range(3):
                p = gray_image[i-1+m, j-1+n]
                s+=p*mask[m][n]
        gray_image[i][j]=s/9


cv2.imshow("media", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
