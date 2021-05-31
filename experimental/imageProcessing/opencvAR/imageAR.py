#
#
#
import numpy as np 
import argparse
import imutils
import sys
import cv2 as cv 
#
##
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
#
src = cv.imread(args["src"])
(srcH, srcW) = src.shape[:2]
#
arUcoDict = cv.aruco.Dictionary_get(cv.aruco.DICT_ARUCO_ORIGINAL)
arUcoParam = cv.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv.aruco.detectMarkers(img, arUcoDict, parameters=arUcoParam)
#
if len(corners) != 4:
    print("Unable to detect corners !!! ")
    sys.exit(0)
#
ids = ids.flatten()
refPts = []
#
for i in (923, 1001, 241, 1007):
    j = np.squeeze(np.where(ids == i))
    corner = np.squeeze(corners[j])
    refPts.append(corner)
#
# Perspective Wrapper
(refptl, refptr, refptbr, refptbl) = refPts
dstMat = [refptl[0], refptr[1], refptbr[2], refptbl[3]]
dstMat = np.array(dstMat)
#
srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])
#
(h, _) = cv.findHomography(srcMat, dstMat)
warped = cv.warpPerspective(src, h, (imgW, imgH))
#
# Applying Mask
mask = np.zeros((imgH, imgW), dtype = "uint8")
cv.fillConvexPoly(mask, dstMat.astype("int32"), (255, 255, 255))
#
maskScaled = mask.copy() / 255.0
maskScaled = np.dstack([maskScaled]*3)
#
warpMultiplied = cv.multiply(warped.astype("float"), maskScaled)
imgMultiplied = cv.multiply(img.astype("float"), 1.0-maskScaled)
output = cv.add(warpMultiplied, imgMultiplied)
output = output.astype("uint8")
#
cv.imshow("Augmented Reality", output)
cv.waitKey(0)
#
#