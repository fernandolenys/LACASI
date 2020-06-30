import cv2
import numpy as np
import math


#image = cv2.imread("C:\\Users\\FERNANDO\\test.jpg")
image = cv2.imread("C:\\Users\\FERNANDO\\test2.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gauss_filter_mask(m,n,sigma):
    r=np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            A=(1 / (2 * math.pi * math.pow(sigma, 2)))
            A=2
            r[i][j]=int(A*(pow(math.e,-((pow(-((m-1)/2-i),2)+pow(-((n-1)/2-j),2))/(2*pow(sigma,2))))))

            print(-(1-i),",",-(1-j)," ")
        print("\n")
    return r

print ('Gray shape:', gray_image.shape)
rows,cols = gray_image.shape


mask=[[1,1,1],
      [1,1,1],
      [1,1,1]]
mask=gauss_filter_mask(3,3,1)
print(mask)

for i in range(1,rows-1):
      for j in range(1,cols-1):
        s=0
        #print (i,j,p)
        for m in range(-1, 2):
            for n in range(-1, 2):
                p = gray_image[i+m, j+n]
                s+=p*mask[m][n]
        gray_image[i][j]=s/9


cv2.imshow("filtro gaussiano", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
