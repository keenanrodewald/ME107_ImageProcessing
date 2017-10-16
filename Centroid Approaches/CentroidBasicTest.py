import numpy as np
import cv2
import MyImageFunctions

cv2.namedWindow('frame')

imageOG = cv2.imread("pics/whiteLine.jpg")
gray = cv2.cvtColor(imageOG, cv2.COLOR_BGR2GRAY)

#MyImageFunctions.MyImageFunctions.whiteBorderGreyIm(gray)


im2, contours, hierarchy = cv2.findContours(gray, 1, 2)

color = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.drawContours(color, contours, -1, (0, 255, 0), 1)

cv2.imshow('frame', color)
cv2.waitKey(0)
