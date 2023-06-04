import cv2
import numpy as np
from markerFinder import findOneContour, findCenter, drawReferencePoint, getReferencePoint, buildSquare

from game.game import game, play, CONTROLLER
from image_deformer import place_image


def dots_from_sequence(sequence, dots_dict):
    dots = []
    for element in sequence:
        if dots_dict[element]:
            dots.append(dots_dict[element])
    return dots

cap = cv2.VideoCapture(1)

cap1 = cv2.VideoCapture(0)


while True:
    tr, frame = cap.read()
    tr, frame_controller = cap1.read()
    
    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur( frame, (40, 40) )
    frame_hsv = cv2.cvtColor(frame_, cv2.COLOR_BGR2HSV)

    frame_controller = cv2.flip(frame_controller, 2)
    frame_ = cv2.blur( frame_controller, (40, 40) )
    frame_hsv_controller = cv2.cvtColor(frame_, cv2.COLOR_BGR2HSV)
    
    ## ! проверить
    #dots = []
    dots_dict = {'red': None, 'blue': None, 'yellow': None, 'green': None}
    # red_controller
    
    clr_low = (0,120,120)
    clr_high = (15,255,255)
    drawReferencePoint(frame_hsv_controller, frame_controller, clr_low, clr_high)
    red_dot = getReferencePoint(frame_hsv_controller, frame_controller, clr_low, clr_high)
    if red_dot :
        cv2.putText(frame_controller, 'YOU', red_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        CONTROLLER.CONTROLLER = red_dot[1]
        
    # red
    
    clr_low = (0,120,120)
    clr_high = (15,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    red_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if red_dot :
        cv2.putText(frame, 'DOT 1', red_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots_dict['red'] = red_dot
        #dots.append(red_dot)


    # blue
    clr_low = (90,120,70)
    clr_high = (140,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    blue_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if blue_dot :
        cv2.putText(frame, 'DOT 2', blue_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots_dict['blue'] = blue_dot
        #dots.append(blue_dot)

    # yellow
    clr_low = (15,110,90)
    clr_high = (35,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    yellow_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if yellow_dot :
        cv2.putText(frame, 'DOT 3', yellow_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots_dict['yellow'] = yellow_dot
        #dots.append(yellow_dot)

    # green
    clr_low = (35,50,90)
    clr_high = (90,255,255)
    drawReferencePoint(frame_hsv, frame, clr_low, clr_high)
    green_dot = getReferencePoint(frame_hsv, frame, clr_low, clr_high)
    if green_dot :
        cv2.putText(frame, 'DOT 4', green_dot , cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv2.LINE_AA)
        dots_dict['green'] = green_dot
        #dots.append(green_dot)

    sequence = ['red', 'blue', 'yellow', 'green']
    dots = dots_from_sequence(sequence, dots_dict)

    buildSquare(frame, dots)

    play()
    try:    
        place_image(frame, game,  dots)
    except:
        pass
    
    cv2.imshow('', frame)
    cv2.imshow('controller', frame_controller)
    key = cv2.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
