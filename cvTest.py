from tkinter import Tk
import cv2 as cv
from cv2 import matchTemplate
import numpy as np
from matplotlib import cm, image, pyplot as plt
from PIL import Image


def MyMatchTempate():
    img=cv.imread("1.PNG",0)
    img2=img.copy()
    template=cv.imread("vip.png",0)
    w,h=template.shape[::-1]
    method=cv.TM_CCOEFF
    res=cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left=max_loc
    bottom_right=(top_left[0]+w, top_left[1]+h)
    cv.rectangle(img,top_left,bottom_right,255,2)
    cv.imshow("p",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotateImage( image, angle ):
    if image != None:
        global dst_image
        dst_image = cv.CloneImage( image )

        rotate_around = (0,0)
        transl = cv.CreateMat(2, 3, cv.CV_32FC1 )

        matrix = cv.GetRotationMatrix2D( rotate_around, angle, 1.0, transl )
        cv.GetQuadrangleSubPix( image, dst_image, transl )
        cv.GetRectSubPix( dst_image, image, rotate_around )
    return dst_image

MyMatchTempate()