import math
import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage import transform
from skimage import  img_as_ubyte

import cv2


def drawDots(cnv, dots):
    for dot in dots:
        cv2.circle(cnv, dot, 5, (0,255,0), -1)

img = data.cat()

SIZE = img.shape[0]+img.shape[1]
cnv = np.zeros( ( SIZE, SIZE, 3), dtype=np.uint8() )

# разместить изо с центром оного по середине
w = img.shape[0]
h = img.shape[1]
cnv[int(h/2):int(h/2)+w,int(w/2):int(w/2)+h,:] = img

img = cnv

cnv = np.ones( ( img.shape[0], img.shape[1], 3), dtype=np.uint8() ) * np.array([210,255,240], dtype=np.uint8())


dst = np.array([[50, 50], [10, 400], [300, 400], [300, 10]])
src = np.array([[0+ int(w/2), 0 + int(h/2)],
                         [0+ int(w/2), 300 + int(h/2)],
                         [451 + int(w/2), 300 + int(h/2)],
                         [451 + int(w/2), 0 + int(h/2)]])


tform3 = transform.ProjectiveTransform()
tform3.estimate(dst, src)

warped = transform.warp(img, tform3, output_shape= (img.shape[0], img.shape[1]))



cat = img_as_ubyte(warped )

cnv = np.where(cat != 0, cat, cnv)

drawDots(cnv, dst)
drawDots(img, src)
cv2.imshow('cat',cat )
cv2.imshow('img',img )
cv2.imshow('cnv',cnv ) 
cv2.waitKey(0)
