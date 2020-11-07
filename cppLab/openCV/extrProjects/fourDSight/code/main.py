import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import math


img_rgb = cv2.imread('StarMap_Original.jpg')  
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('Small_area.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold, _ = cv2.threshold(template,127,255,cv2.THRESH_BINARY)
threshold = threshold/255
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
#    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.circle(img_rgb, (pt[0], pt[1]), 2, (0,255,0), 2)
    cv2.circle(img_rgb, (pt[0], pt[1]+h), 2, (0,255,0), 2)
    cv2.circle(img_rgb, (pt[0]+w, pt[1]), 2, (0,255,0), 2)
    cv2.circle(img_rgb, (pt[0]+w, pt[1]+h), 2, (0,255,0), 2)


cv2.imwrite('py_Small_area_result.png',img_rgb)
plt.imshow(img_rgb)
plt.title('Small Non-Rotated Area Detection')
plt.show()



img_rgb = cv2.imread('StarMap_Original.jpg')  
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('Small_area_rotated.jpg',0)

for i in range(0,4):
    template = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)

    w, h = template.shape[::-1]
    template = template[0:h-2, 0:w-2]


 #   threshold = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
 #   threshold, _ = cv2.threshold(template,127,255,cv2.THRESH_BINARY)
 #   threshold = threshold/255

    threshold = 0.3
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    loc = np.where( res >= threshold)

    loc_np = np.asarray(loc) 
    print(loc_np.size )
    if loc_np.size != 0:
        for pt in zip(*loc[::-1]):
            cv2.circle(img_rgb, (pt[0], pt[1]), 2, (0,255,0), 2)
            cv2.circle(img_rgb, (pt[0], pt[1]+h), 2, (0,255,0), 2)
            cv2.circle(img_rgb, (pt[0]+w, pt[1]), 2, (0,255,0), 2)
            cv2.circle(img_rgb, (pt[0]+w, pt[1]+h), 2, (0,255,0), 2)
        cv2.imwrite('py_Small_area_rotated_result_'+str(i*90)+'.png',img_rgb)
        plt.imshow(img_rgb)
        plt.title('Small Rotated Area Detection')
        plt.show()





