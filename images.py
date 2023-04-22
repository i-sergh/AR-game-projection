import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage import transform
from skimage import img_as_float, img_as_ubyte

import cv2

slider_window =  np.zeros( ( 500, 600, 3), dtype=np.uint8() )

img = data.chelsea()
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img = np.where(img == (0,0,0), (1,1,1), img)
# подготовить новый квадратный массив img.shape[0]*img.shape[1] x img.shape[0]*img.shape[1]
SIZE = img.shape[0]+img.shape[1]
cnv = np.zeros( ( SIZE, SIZE, 3), dtype=np.uint8() )

# разместить изо с центром оного по середине
w = img.shape[0]
h = img.shape[1]
cnv[int(h/2):int(h/2)+w,int(w/2):int(w/2)+h,:] = img


# не забыть img_as_float, а нужно ли

matrix = np.array([ [1., 0, 0],
                               [0, 1., 0],
                               [0, 0, 1.] ])
print(matrix.dtype)
tform = transform.ProjectiveTransform(matrix=matrix)
tf_img = transform.warp(cnv, tform.inverse)



def on_changeY2X0(value):
    value = (value - 100) / 100000
    matrix[2,0] = value

def on_changeY2X1(value):
    value = (value - 100) / 100000
    matrix[2,1] = value

def on_changeY0X2(value):
    value = (value - 200)* 10
    matrix[0,2] = value

def on_changeY1X2(value):
    value = (value - 200)* 10 
    matrix[1,2] = value


def on_changeY1X1(value):
    value = (value - 200) /100 
    matrix[1,1] = value
    print(matrix)

def on_changeY0X0(value):
    value = (value - 200) /100 
    matrix[0,0] = value

def on_changeY1X0(value):
    value = (value - 200) /100 
    matrix[1,0] = value


def on_changeY0X1(value):
    value = (value - 200) /100 
    matrix[0,1] = value   
    
cv2.namedWindow('sliders')
cv2.createTrackbar('y2 x0', 'sliders', 100, 200, on_changeY2X0)
cv2.createTrackbar('y2 x1', 'sliders', 100, 200, on_changeY2X1)

cv2.createTrackbar('y1 x1', 'sliders', 300, 400, on_changeY1X1)
cv2.createTrackbar('y0 x0', 'sliders', 300, 400, on_changeY0X0)
cv2.createTrackbar('y1 x0', 'sliders', 200, 400, on_changeY1X0)
cv2.createTrackbar('y0 x1', 'sliders', 200, 400, on_changeY0X1)

cv2.createTrackbar('y0 x2', 'sliders', 200, 400, on_changeY0X2)
cv2.createTrackbar('y1 x2', 'sliders', 200, 400, on_changeY1X2)
# в uint8 !!!RGB!!!
new_img = img_as_ubyte(tf_img )

while True:
    try:
        tform = transform.ProjectiveTransform(matrix=matrix)
        tf_img = transform.warp(cnv, tform.inverse)
    except:
        pass
    new_img = img_as_ubyte(tf_img )
    cv2.imshow('sliders',slider_window)
    cv2.imshow('cat',new_img ) 
    
    key = cv2.waitKey(1)

    if key == 27:
        break
cv2.destroyAllWindows()




