import cv2

#Start webcam capture
cv2.namedWindow('frame')

testFrame = cv2.imread("pics/ThickLine.jpg")
shape = testFrame.shape
height = shape[0]
length = shape[1]
divisions = 6
rowHeight = round(height / divisions)
print(rowHeight)


def splitImageRows(image, numRows):
    # Find length and height of input image
    shape = image.shape
    height = shape[0]
    rowHeight = round(height / numRows)
    # Create imRows list and start a counter for y position
    imRows = []
    ycount = 0
    # Iterate through each row and append each new row image to imRows list
    for i in range(0, numRows - 1):
        imRows.append(image[ycount: ycount + rowHeight, :])
        ycount += rowHeight
    return imRows

#Function that will process the raw image
def imageProcessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY )
    #Need to invert because original image was black line on white background
    thresh = (255 - thresh)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    eroded = cv2.erode(thresh, kernel)
    return eroded



processed = imageProcessing(testFrame)



rows = splitImageRows(processed, 6)
#Splits off bottom row of image and finds contours
bottomRow = rows[4]
im2, contours, hierarchy = cv2.findContours(processed, 1, 2)

#converts image back to color and draws found contours
color = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
cv2.drawContours(color, contours, -1, (0, 255, 0), 3)

cv2.imshow('frame', bottomRow)
cv2.waitKey(0)


