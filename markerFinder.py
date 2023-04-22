import cv2
import numpy as np


def findOneContour(clr_low, clr_high, img_hsv):
    mask = cv2.inRange(img_hsv, clr_low, clr_high)
    
    cont, h = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
    cont = sorted( cont,key=cv2.contourArea, reverse=True)
    if len(cont)> 0:
        cn = cont[0]
        if cv2.contourArea(cn) > 100:
            return [cn]
        else:
            return []
    else:
        return []
            
def findCenter (clr_mask):
    moments = cv2.moments(clr_mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    x = int(dM10 / dArea)
    y = int(dM01 / dArea)
    return (x, y)

def  drawReferencePoint(frame_hsv, canvas, clr_low, clr_high):
    clr_cont = findOneContour( clr_low, clr_high, frame_hsv ) 
    if len(clr_cont) > 0:
        cv2.drawContours(canvas, clr_cont, -1, (0,255,0), 2)
        clr_cont_mask = np.zeros( (canvas.shape[0], canvas.shape[1] ), dtype=np.uint8() ) 
        cv2.drawContours(clr_cont_mask, clr_cont, -1, 255, -1)
        x, y = findCenter (clr_cont_mask)
        cv2.circle(canvas, (x, y), 10, (0,0,255), -1)


def  getReferencePoint(frame_hsv, canvas, clr_low, clr_high):    
    clr_cont = findOneContour( clr_low, clr_high, frame_hsv ) 
    if len(clr_cont) > 0:
        clr_cont_mask = np.zeros( (canvas.shape[0], canvas.shape[1] ), dtype=np.uint8() ) 
        cv2.drawContours(clr_cont_mask, clr_cont, -1, 255, -1)
        x, y = findCenter (clr_cont_mask)
        return(x,y)
    return ()

def getLineDots(dots):
    return [ (dots[0], dots[1]),
                 (dots[1], dots[2]),
                 (dots[2], dots[3]),
                 (dots[3], dots[0])]

def getCenterOfLine(startDot, endDot):
    x = int((startDot[0] + endDot[0])/2)
    y = int((startDot[1] + endDot[1])/2)
    return (x,y)

def buildSquare(img, dots_):
    if len(dots_) == 4:
        dots = dots_.copy()
        dots.append(dots[0])
        centersOfLines = []
        for  pair_dot in  getLineDots(dots):
            cv2.line(img, pair_dot[0], pair_dot[1], (200,0,255), 2)
            x,y = getCenterOfLine(pair_dot[0], pair_dot[1])
            centersOfLines.append((x,y))
            cv2.circle(img, (x, y), 5, (255,0,0), -1)

        cv2.line(img, centersOfLines[0], centersOfLines[2], (200,0,100), 2)
        cv2.line(img, centersOfLines[1], centersOfLines[3], (200,0,100), 2)
        
            
