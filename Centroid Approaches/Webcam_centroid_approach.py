import numpy as np
import cv2

#Start webcam capture
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

ret1, testFrame = cap.read()
shape = testFrame.shape
height = shape[0]
length = shape[1]
divisions = 6
rowHeight = round(height / divisions)
print(rowHeight)

#Function that will process the raw image
def imageProcessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh

while(True):
    ret, frame = cap.read()
    processed = imageProcessing(frame)

    #Splits off bottom row of image and finds contours
    bottomRow = processed[height-rowHeight:height, :]
    im2, contours, hierarchy = cv2.findContours(bottomRow, 1, 2)

    #converts image back to color and draws found contours
    color = cv2.cvtColor(bottomRow, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(color, contours[0], -1, (0, 255, 0), 3)
    cv2.imshow('frame', color)