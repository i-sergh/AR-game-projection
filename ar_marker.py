import cv2
import numpy as np
from markerFinder import findOneContour, findCenter, drawReferencePoint, getReferencePoint, buildSquare

from game.game import game, play
from image_deformer import place_image


cap = cv2.VideoCapture(0)

while True:
    tr, frame = cap.read()
    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur( frame, (40, 40) )
    frame_hsv = cv2.cvtColor(frame_, cv2.COLOR_BGR2HSV)
    dots = []
    # red
    clr_low = (0,90,20)
    clr_high = (15,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    red_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if red_dot :
        cv2.putText(frame, 'DOT 1', red_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots.append(red_dot)

    # blue
    clr_low = (90,120,70)
    clr_high = (140,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    blue_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if blue_dot :
        cv2.putText(frame, 'DOT 2', blue_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots.append(blue_dot)

    # yellow
    clr_low = (15,110,90)
    clr_high = (35,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    yellow_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if yellow_dot :
        cv2.putText(frame, 'DOT 3', yellow_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots.append(yellow_dot)

    # green
    clr_low = (35,50,90)
    clr_high = (90,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    green_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if green_dot :
        cv2.putText(frame, 'DOT 4', green_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots.append(green_dot)

    buildSquare(frame, dots)

    play()
    place_image(frame, game,  dots)
        
    cv2.imshow('', frame)

    key = cv2.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
