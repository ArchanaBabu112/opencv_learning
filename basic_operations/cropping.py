import os
import cv2

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\bird1.jpg"

img= cv2.imread(image_path)

print(img.shape)

cropped_imag= img[90:183, 74:148 ]
cv2.imshow('img', img)
cv2.imshow('cropped_imag', cropped_imag)
cv2.waitKey(0)

