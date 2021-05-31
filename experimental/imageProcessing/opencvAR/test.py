#
#
#
import numpy as np 
import argparse
import imutils
import sys
import cv2 as cv 
#
#
# initialize the argument parser
ap = argparse.ArgumentParser()  
#
ap.add_argument("-i", "--img", required = True)
ap.add_argument("-s", "--src", required=True)
args = vars(ap.parse_args())
#
img = cv.imread(args["img"])
img = imutils.resize(img, width=600)
(imgH, imgW) = img.shape[:2]
src = cv.imread(args["src"])
#
cv.imshow("Augmented Reality", src)
cv.waitKey(0)

cv.imshow("Augmented Reality", img)
cv.waitKey(0)