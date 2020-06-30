import cv2
import numpy as np

#image = cv2.imread("C:\\Users\\FERNANDO\\test.jpg")
image = cv2.imread("C:\\Users\\FERNANDO\\test2.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


print ('Gray shape:', gray_image.shape)
rows,cols = gray_image.shape
hist=np.zeros([256], dtype=int)
for i in range(rows):
      for j in range(cols):
            hist[gray_image[i][j]]+=1

h = np.ones((300,255,3),np.uint8)*255

for i in range(255):
            cv2.line(h, (i, 300), (i, int(300-hist[i]/5)), (250,100,100), thickness=2)

cv2.imshow('histograma',h)

cv2.imshow("image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()