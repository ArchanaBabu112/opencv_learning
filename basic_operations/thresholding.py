# 2 types of thresholding in opencv
# simple thresholding and adaptive thresholding
#  we hv to use multiple threshoulds in a single image on each part of the img, threshold value will be different


import os, cv2

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\handwritten.jpg"

img= cv2.imread(image_path)
img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh= cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
# ret, thresh= cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
ret, simple_thresh= cv2.threshold(img_gray, 80,255,cv2.THRESH_BINARY)

# If pixel value > 80 → set to 255
# If pixel value ≤ 80 → set to 0

# thresh= cv2.blur(thresh, (10,10))
# ret, thresh= cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('img:', img)
cv2.imshow("adaptive threshold:",adaptive_thresh)
cv2.imshow('thresh:', simple_thresh) # thresholding is using for segmantation of image into different region
#  adaptive threshould is better
cv2.waitKey(0)