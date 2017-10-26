import numpy as np
import cv2
import Keenan.MyImageFunctions as myimfun

#Start webcam capture
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

while(True):
    # get current frame frmo video capture
    ret1, currFrame = cap.read()
    # first greyscale, then threhold and erode the image
    numRows = 6
    centroidArr = myimfun.imToCentroidArray(currFrame, numRows)

    myimfun.showRows(currFrame, numRows)
    myimfun.showCentroids(currFrame, numRows, centroidArr)

    cv2.imshow('frame', currFrame)
    cv2.waitKey(0)

    """ converts image back to color and draws found contours
    color = cv2.cvtColor(bottomRow, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(color, contours[0], -1, (0, 255, 0), 3)
    cv2.imshow('frame', color) """