import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Any
from logzero import logger 
from chaoslib.types import Configuration, Secrets,Activity
from chaoslib.exceptions import ActivityFailed, InvalidActivity


__all__ = ["zoomcvimage"]

img = cv2.imread('Simul1.PNG',0)
img2 = cv2.imread('Simul1.PNG')
img2 = cv2.resize(img2,(1000,500))

# global thresholding
ret1,th1 = cv2.threshold(img,1000,1200,cv2.THRESH_BINARY)


ret,thresh3= cv2.threshold(img,200,200,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cells = [np.hsplit(row,500) for row in np.vsplit(gray,100)]
x = np.array(cells)
print('Array',x)

print("Images",img)
#edges = cv2.Canny(th1,2000,2000)
#print("Edges",edges)
rows,cols = img.shape
#kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(img,kernel,iterations = 10)
#print(erosion)
#M = np.float32([[1,0.25,100],[0.5,1,50]])

val=input("Enter a number:")
num1=int(val)


def zoomcvimage(i,configuration: Configuration=None,secrets: Secrets=None)->None:
 for i in range(num1):
  M = cv2.getRotationMatrix2D((cols/2,rows/2),i,i)
  dst = cv2.warpAffine(thresh4,M,(cols,rows))
  cv2.imshow('img',dst)
  cv2.waitKey(123)
  cv2.imwrite("CVplot.png",dst)
  plt.imshow(dst)
plt.show()
cv2.waitKey(230)
pass

zoomcvimage(num1)

def featureextract(img2):
 imheight=img2.shape[0]
 print("Height",imheight)
 imwidth=img2.shape[1]
 print("Width",imwidth)

 y1 = 0
 M = imheight//20
 N = imwidth//20

#for y in range(0,imheight,M):
#    for x in range(0, imwidth, N):
#        y1 = y + M
#        x1 = x + N
#        tiles = img2[y+int(M/4):y+M,x+int(N/4):x+N]
#        cv2.rectangle(img2, (y, x), (y1,x1), (0,1,0))
#        cv2.imwrite("save/" + str(y) + '_' + str(x)+".png",tiles)


 print("Images",img2)
#print("Tiles size",tiles.size)



 for y in range(0,imheight,M):
  for x in range(0,imwidth,N):
         y1 = y + M
         x1 = x + N
         tiles = img2[y:y+M,x:x+N]
         cv2.rectangle(img2, (x,y), (x1,y1), (0,255,0))
         cv2.imwrite("save/" + str(x) + '_' + str(y)+".png",tiles)
         cv2.imwrite("SimulationGrid.png",tiles)


#img3=img2[2:random.randint(10,2000),2:random.randint(10,2000)]


 a=random.randint(1,100)
 b=random.randint(100,1000)
 c=random.randint(1,100)
 d=random.randint(100,1000)



#for y in range(0, 200*a,M):
#  for x in range(0,200*b,N):
#   if ((b>a) and (d>c)):
#       tiles=img2[a:b+N,b:d+M]
#       cv2.imwrite("SimulationGrid.png",tiles) 
#   else:
#       tiles=img2[b:a,d:c]
#      cv2.imwrite("SimulationGrid.png",tiles)


#v2.imwrite("SimulGrid.png",img2) 
#plt.plot(th1)
#plt.imshow(th1)
 print(img2.size)
#plt.imshow(img2[10:200,10:200],cmap = 'gray')

#img3= cv2.vconcat(img2[10:100,10:100],img2[0:10,0:10])
#img3 = cv2.hconcat(img2[10:100,10:100],img2[0:10,0:10])
#plt.imshow(img3)
#print("Concatenated image shape",img3.shape)
 print("Dst Magnified",img2)
#plt.imshow(cells)
#kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
#img2 = cv2.filter2D(img2, -1, kernel)
 plt.imshow(img2)
 plt.show()
 cv2.waitKey(123)

featureextract(img2)
