import numpy as np
import cv2
img=np.zeros((120,400,3), np.uint8) 			#创建一幅黑色图像
def doChange(x):
    b=cv2.getTrackbarPos('B','tracebar')
    g=cv2.getTrackbarPos('G','tracebar')
    r=cv2.getTrackbarPos('R','tracebar')
    img[:]=[b,g,r]                          			#更改图像
cv2.namedWindow('tracebar')
cv2.createTrackbar('B','tracebar',0,255,doChange)	#创建跟踪栏
cv2.createTrackbar('G','tracebar',0,255,doChange)
cv2.createTrackbar('R','tracebar',0,255,doChange)
while(True):
    cv2.imshow('tracebar',img)           			#显示图像
    k = cv2.waitKey(1)
    if k == 27:                         			#按【Esc】键时结束循环
        break
cv2.destroyAllWindows()
