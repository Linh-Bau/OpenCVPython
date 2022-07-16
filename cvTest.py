from cmath import sin
from datetime import time
from tkinter import Tk
from turtle import color
import cv2 as cv
from cv2 import matchTemplate
import cv2
from cv2 import sqrt
import numpy as np
from matplotlib import cm, image, pyplot as plt
from PIL import Image
from scipy import ndimage
from datetime import datetime
import math as mat


def myF(r,g,b,a):
    value=a+(3*(r-a)*(r-a)+(g-a)*(g-a)+(b-a)*(b-a))/a
    if(value>255):
        return 255
    else:
        return value

def TestFuction1():
    img=cv.imread('1.PNG')
    r_img=img[:, :, 0]
    g_img=img[:, :, 1]
    b_img=img[:, :, 2]
    
    g_img=cv.imread('vip.PNG',0)
    ret, des=cv.threshold(g_img,150,255,cv.THRESH_BINARY)
    row, col=r_img.shape
    # for i in range(row):
    #     for j in range(col):
    #         average_value=(r_img[i,j]+g_img[i,j]+b_img[i,j])/3
    #         g_img[i,j]=myF(r_img[i,j], g_img[i,j], b_img[i,j], average_value)
    cv.imshow("p",des)
    cv.waitKey(0)
    cv.destroyAllWindows()

def TestFuction():
    g_img=cv.imread('vip.PNG',0)
    value=[i for i in range(50,200,10)]
    for v in value:
        ret, des=cv.threshold(g_img,v,255,cv.THRESH_BINARY)
        cv.imshow("p",des)
        cv.waitKey(0)
    cv.destroyAllWindows()

def SupperFind():
    #rotate 360
    start=datetime.now()
    print("start test ",start.time())
    deg=[i for i in range(0,359,10)]
    img_rgb=cv.imread("1.PNG")
    img_gray=cv.imread("1.PNG",0)
    template=cv.imread("vip.png",0)
    max_val, top_left, bottom_right, _deg=0,0,0,0
    best_result=None
    for d in deg:
        output=myRotate(img_gray,d)
        max,top,botton=MyMatchTempate(output,template)
        if(max>max_val):
            max_val=max
            top_left=top
            bottom_right=botton
            _deg=d
            rotate_rgb=myRotate(img_rgb,d)
            best_result=cv.rectangle(rotate_rgb,top_left,bottom_right,color=(0,255,0),thickness=3)
    best_result=myRotate(best_result,360-_deg)
    print("end test ",datetime.now().time())
    cv.imshow("p",best_result)
    cv.waitKey(0)
    cv.destroyAllWindows()


def drawTest():
    img_rgb=cv.imread("1.PNG")
    img=cv.rectangle(img_rgb,(100,100),(500,500),color=(255,0,100),thickness=3)
    img2=myRotate(img,30)
    img2=cv.rectangle(img2,(100,100),(500,500),color=(255,0,100),thickness=3)
    cv.imshow("p",img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

def myRotate(image,degree:np.double):
    global vvv
    vvv= ndimage.rotate(image,degree,reshape=True,mode='constant')
    return vvv



def MyMatchTempate(img,template):
    w,h=template.shape[::-1]
    method=cv.TM_CCOEFF
    res=cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left=max_loc
    bottom_right=(top_left[0]+w, top_left[1]+h)
    return max_val,top_left,bottom_right

# def rotateImage( image, angle ):
#     if image != None:
#         global dst_image
#         dst_image = cv.CloneImage( image )

#         rotate_around = (0,0)
#         transl = cv.CreateMat(2, 3, cv.CV_32FC1 )

#         matrix = cv.GetRotationMatrix2D( rotate_around, angle, 1.0, transl )
#         cv.GetQuadrangleSubPix( image, dst_image, transl )
#         cv.GetRectSubPix( dst_image, image, rotate_around )
#     return dst_image

SupperFind()