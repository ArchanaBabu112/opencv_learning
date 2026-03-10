import cv2
import os

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\bird1.jpg"
img= cv2.imread(image_path)
resized_img= cv2.resize(img, (296, 266 )) # w, h

print(resized_img.shape) #h, w

cv2.imshow('img', img)
cv2.imshow("resized_img", resized_img)
cv2.waitKey(0)