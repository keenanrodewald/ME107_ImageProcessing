import numpy as np
import cv2


# Capture frame-by-frame
filePath = 'pics/ThickLine.jpg'
img = cv2.imread(filePath)

def imageProcessing(image):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    kernel = 1 / 5 * np.ones((3, 3), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closing_neg = cv2.bitwise_not(closing)

    finalProcessIm = closing_neg
    return finalProcessIm


def nothing(x):
    pass
cv2.namedWindow('window')
cv2.createTrackbar('trackbar', 'window', 350, 500,nothing)

# Trying a couple dilation techniques here

processed = imageProcessing(img)

#while needed so that trackbar can work continuously
while True:
    img = cv2.imread(filePath)
    threshold = cv2.getTrackbarPos('trackbar', 'window')

    minLineLength = 500
    maxLineGap = 0
    lines = cv2.HoughLinesP(processed, 1, np.pi / 180, threshold, minLineLength, maxLineGap)

    if lines is not None:
        for line in lines[0:3]:
            for x1, y1, x2, y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Trackbar Value: " + str(threshold), (50, 50), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('window', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(lines)
        break
