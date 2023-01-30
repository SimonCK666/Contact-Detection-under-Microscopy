'''
Author: Simon Yang SimonYang223@163.com
Date: 2023-01-30 16:40:50
LastEditors: Simon Yang SimonYang223@163.com
LastEditTime: 2023-01-30 17:23:25
FilePath: \Contact-Detection-under-Microscopy\detectPipette.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import cv2
import numpy as np

img = cv2.imread("E:\\Contact Detection\\Contact-Detection-under-Microscopy\\img\\micropipette.jpg", 0)

# Perform Gaussian Blur
blur = cv2.GaussianBlur(img,(5,5),0)

# Perform OTSU Algorithm
ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Create the structuring element
kernel = np.ones((5,5), np.uint8)

# Perform morphological close operation
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Morphological Image", thresh)

# Find contours in the image
contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Show the image with the contours
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
