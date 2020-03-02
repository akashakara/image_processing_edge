import cv2
import matplotlib as plt
import numpy

img=cv2.imread("test2.jpg")
resiz_e=cv2.resize(img,(0,0),fx=0.20,fy=0.20)
edge_img=cv2.Canny(resiz_e,100,200)
print(edge_img)
cv2.imshow("edge image",edge_img)
cv2.waitKey(0)

