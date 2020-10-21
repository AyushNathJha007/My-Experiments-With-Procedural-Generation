# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:22:42 2020

@author: LENOVO
"""
'''from PIL import Image,ImageDraw

im=Image.open('mario-1-1.jpg')

max_w,max_h=im.size
X=16
Y=215
draw=ImageDraw.Draw(im)
while X<=max_w:
    draw.line((X,0,X,max_h),fill=255)
    X+=16
while Y>=0:
    draw.line((0,Y,max_w,Y),fill=255)
    Y-=16
del draw
im.show()'''

import cv2
im=cv2.imread('mario-1-1.jpg')
img=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
max_Y,max_X=img.shape
X=16
Y=8
while X<=max_X:
    cv2.line(img,(X,0),(X,max_Y),(255,0,0))
    X+=16
while Y<=max_Y:
    cv2.line(img,(0,Y),(max_X,Y),(255,0,0))
    Y+=16
cropImg=img[8:24,0:16].copy()
k=cv2.resize(cropImg,(16,16))
cv2.imshow("img",k)
cv2.waitKey(0)
cv2.destroyAllWindows()