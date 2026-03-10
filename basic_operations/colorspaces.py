import os
import cv2


image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\bird1.jpg"

img= cv2.imread(image_path)
# img_bw=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #everything from B changes to R, like wise other colors
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #everything from B changes to R, like wise other colors
# HSV:- Hue(color Type) Saturation(color intensity) Value(brightness)
#  to convert an image from one clor space to another
# img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #everything from B changes to R, like wise other colors
cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)
#  in opencv all images are in a combinations of BGR