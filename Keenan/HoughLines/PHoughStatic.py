import numpy as np
import cv2



# Capture frame-by-frame
img = cv2.imread('Keenan/pics/GraphPic.jpg')

# Our operations on the frame come here
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

#creates an array of line values
minLineLength = 10
maxLineGap = 100
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 1, minLineLength, maxLineGap)

if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


# Display the resulting frame
cv2.imwrite('houghlines5.jpg', img)

print(lines)
