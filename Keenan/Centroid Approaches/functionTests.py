import numpy as np
import cv2
import Keenan.MyImageFunctions as myimfun




# get current frame frmo video capture
currFrame = cv2.imread("turn1.png")
# first greyscale, then threhold and erode the image
numRows = 10
centroidArr = myimfun.imToCentroidArray(currFrame, numRows)

myimfun.showRows(currFrame, numRows)
myimfun.showCentroids(currFrame, numRows, centroidArr)

errorArray = myimfun.centroidToError(centroidArr, currFrame)
print(errorArray)

cv2.imshow('frame', currFrame)
cv2.waitKey(0)
