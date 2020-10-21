import cv2
from skimage import measure
from PIL import Image,ImageDraw
import csv
import os
import sys

symbols=["G","S","B","#","#","F","P","?","#","#","*","P","P","P","#","?","G","S","B","P","P","P","P","P","P"]
print(len(symbols))         
path="blockimgs/"

block_imgs=[]

ssim_vals=[]

for i in range (1,26):
    ImgFullPath=path+str(i)+".png"
    block_imgs.append(ImgFullPath)

   
def compareImages(CroppedImage):
    ssim_vals.clear()
    for i in range(0,25):
        imageA=cv2.imread(block_imgs[i])
        gA=cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        rgA=cv2.resize(gA,(16,16))
        gCroppedImage=cv2.cvtColor(CroppedImage, cv2.COLOR_BGR2GRAY)
        rgCroppedImage=cv2.resize(gCroppedImage,(16,16))
        ssim_vals.append(measure.compare_ssim(rgCroppedImage,rgA))
    if max(ssim_vals)<0.5: 
        return 10
    else:
        return ssim_vals.index(max(ssim_vals))

def main():
    img=cv2.imread('SuperMarioBros_Maps/mario-2-1.jpg')
    f = open("mario-2-1_t.csv", "w")
    im=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    max_Y,max_X=im.shape
    '''for i in range(7,max_Y-16,16):
        li=""
        for j in range(16,max_X-16,16):
            if i>max_Y or j>max_X:
                break
            cropImg=img[i:i+16,j:j+16].copy()
    #cropImg=img[8:24,0:16].copy()
            li+=symbols[compareImages(cropImg)]'''
    for i in range(16,max_X-16,16):
        li=""
        for j in range(7,max_Y-16,16):
            if i>max_X or j>max_Y:
                break
            cropImg=img[j:j+16,i:i+16].copy()
    #cropImg=img[8:24,0:16].copy()
            li+=symbols[compareImages(cropImg)]
        f.write(li)
        f.write("\n")
    f.close()
    '''k=cv2.resize(cropImg,(16,16))
    cv2.imshow("img",k)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

if __name__ == "__main__":
    main()