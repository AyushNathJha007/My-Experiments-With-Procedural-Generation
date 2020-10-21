# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:01:59 2020

@author: LENOVO
"""

import cv2
from skimage import measure
from PIL import Image,ImageDraw
from resizeimage import resizeimage
imageA = cv2.imread('mario-1-1.jpg')
imageB = cv2.imread('mario-1-1.jpg')

# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

#cv2.imshow("im",im)
im=Image.open('mario-1-1.jpg')
imr=resizeimage.resize_cover(im,[16,16])
im2=Image.open('mario-1-1.jpg')

gA=cv2.cvtColor(imr, cv2.COLOR_BGR2GRAY)

path="../blockimgs/"

symbols=["G","S","B","#","#","F","P","?","#","#","*","P","P","P"]
block_imgs=[]

for i in range (1,15):
    ImgFullPath=path+str(i)+".png"
    block_imgs.append(ImgFullPath)

#print(block_imgs)
n=measure.compare_ssim(grayA,grayB)
print(n)