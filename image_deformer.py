from skimage import data
from skimage import transform
from skimage import  img_as_ubyte

import numpy as np
import cv2

def drawDots(cnv, dots):
    for dot in dots:
        cv2.circle(cnv, dot, 5, (0,255,0), -1)


def place_image(cnv, img, dots):
    if len(dots) < 4:
        return None
    
    img_layer = np.zeros( cnv.shape, dtype = np.uint8() )


    dst = np.array([[0, 0], [0, img.shape[0]], [img.shape[1], img.shape[0]], [img.shape[1], 0]])
    drawDots(img, dst)
    src = np.array(dots)


    tform3 = transform.ProjectiveTransform()
    tform3.estimate( src, dst)

    warped = transform.warp(img, tform3, output_shape= (cnv.shape[0], cnv.shape[1]))

    cat = img_as_ubyte(warped )
    
    cnv[cat != 0] =  cat[cat != 0] 



if __name__ == '__main__':
    
    cnv = np.zeros((600, 600, 3), dtype=np.uint8())
    img = data.cat()
    dots = [[50, 50], [10, 400], [300, 400], [300, 10]]
    
    place_image(cnv, img, dots)
    drawDots(cnv, dots)
    cv2.imshow('cnv', cnv)
    cv2.imshow('cat', img)
    cv2.waitKey(0)
