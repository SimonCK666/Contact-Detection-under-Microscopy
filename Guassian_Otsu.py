'''
Author: Simon Yang SimonYang223@163.com
Date: 2023-01-30 16:40:50
LastEditors: Simon Yang SimonYang223@163.com
LastEditTime: 2023-01-30 17:00:06
FilePath: \Contact-Detection-under-Microscopy\Guassian_Otsu.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

'''
In the above code, the input image is first blurred using a Gaussian blur 
to reduce noise. Then, the cv2.adaptiveThreshold function is used to apply 
Otsu's Adaptive Thresholding, where 255 is the maximum pixel value, 
cv2.ADAPTIVE_THRESH_OTSU specifies the use of Otsu's method, cv2.THRESH_BINARY
specifies binary thresholding, 11 is the size of the neighborhood used to 
calculate the threshold, and 2 is the constant subtracted from the mean.
'''
import cv2
import numpy as np

img = cv2.imread("E:\\Contact Detection\\Contact-Detection-under-Microscopy\\img\\micropipette.jpg", 0)

blur = cv2.GaussianBlur(img,(5,5),0)
ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
