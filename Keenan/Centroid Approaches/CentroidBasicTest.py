import cv2
import Keenan.MyImageFunctions as imfun

cv2.namedWindow('frame')

imageOG = cv2.imread("whiteLine.jpg")
centArr = imfun.imToCentroidArray(imageOG, 6)

cv2.imshow('frame', imageOG)
cv2.waitKey(0)

print(centArr)
