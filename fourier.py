import cmath
import math
import cv2
import numpy as np
import os
image=cv2.imread("C:\\Users\\FERNANDO\\f.png")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rows,cols=gray_image.shape
result=np.zeros((rows,cols))
inverse=np.zeros((rows,cols))
F=np.zeros((rows,cols))
t=(cols**2)*(rows**2)
a=0;
for i in range(0,rows):
    for j in range(0,cols):
        s=0;
        s2=0;
        for y in range(0,rows):
            for x in range(0,cols):
                #        1/MN     *     f(x)       *     -1^(x+y) *                exp(-j2r* ux/M+  vy/N)
                aux=((-1)**(x+y))
                aux2=(1/(rows*cols))* gray_image[y][x]* cmath.exp(complex(-1j)*2*math.pi*(i*y/rows+j*x/cols))
                s+=aux2*aux
                s2+=aux2
                a+=1
                print('transformada direta: {:.2f}%'.format( a/t*100))
        F[i][j]=s2
        result[i][j]=math.sqrt(s.real**2 + s.imag**2)
a=0
for i in range(0,rows):
    for j in range(0,cols):
        s=0;
        for u in range(0,rows):
            for v in range(0,cols):
                s +=(1/(rows*cols))*F[u][v]  * cmath.exp(complex(1j) * 2 * math.pi * (i * u / rows + j * v / cols))
                a+=1
                print('transformada inversa: {:.2f}%'.format(a / t * 100))
        inverse[i][j] = s



cv2.imshow("espectro", result)
cv2.imshow("original",inverse)
cv2.waitKey(0)
cv2.destroyAllWindows()