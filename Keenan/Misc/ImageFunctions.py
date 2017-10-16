import numpy as np
import cv2


class ImageFunctions:

    def __init__(self):
        return

    @staticmethod
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

    @staticmethod
    def threshErode(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # Need to invert because original image was black line on white background
        thresh = (255 - thresh)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        eroded = cv2.erode(thresh, kernel)
        return eroded

    @staticmethod
    def adaptiveThreshErode(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        # Need to invert because original image was black line on white background
        thresh = (255 - thresh)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        eroded = cv2.erode(thresh, kernel)
        return eroded

    # initializer for using webcam : not sure if this will work since cap may only be defined within this script.
    @staticmethod
    def startWebcam(self):
        cap = cv2.VideoCapture(0)
        cv2.namedWindow('frame')

    # converts each border pixel to white
    # TODO: Check if this works to close features for feature detection
    #Todo: check whether I need to index from imHeight-1 or just imHeight
    @staticmethod
    def whiteBorderGreyIm(image):
        imHeight = image.shape[0]
        imWidth = image.shape[1]
        # top row
        image[0:imWidth, 0] = 255
        # right row
        image[imWidth - 1, 0:imHeight] = 255
        # bottom row
        image[0:imWidth-1, imHeight-1] = 255
        # left row
        image[0, 0:imHeight-1] = 255

        return

