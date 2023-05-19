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



matrix = np.array([ [1., 0, 0],
                               [0, 1., 0],
                               [0,  0,0.5] ])

tform = transform.ProjectiveTransform(matrix=matrix)
tf_img = transform.warp(cnv, tform.inverse)
new_img = img_as_ubyte(tf_img )
new_img[int(h/2):int(h/2)+w,int(w/2):int(w/2)+h,1] = img[:,:,1]
cv2.imshow('cat',new_img ) 
cv2.waitKey(0)
