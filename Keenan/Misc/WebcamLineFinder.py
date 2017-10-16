import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

#required for the trackbar
def nothing(x):
    pass

cv2.createTrackbar('trackbar', 'frame', 351, 500,nothing)

def imageProcessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = 1 / 5 * np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closing_neg = cv2.bitwise_not(closing)

    finalProcessIm = closing_neg
    return finalProcessIm


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    processed = imageProcessing(frame)

    #creates an array of line values
    minLineLength = 50
    maxLineGap = 5
    lines = cv2.HoughLinesP(processed, 1, np.pi / 180, cv2.getTrackbarPos('trackbar', 'frame'), minLineLength, maxLineGap)

    frameToShow = processed
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(frameToShow, (x1, y1), (x2, y2), (0, 255, 0), 2)



    # Display the resulting frame
    cv2.imshow('frame',frameToShow)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('GraphPic.jpg', frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()