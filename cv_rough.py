import cv2
import os

# reading img
# image_path= os.path.join('bird1.jpg')

img= cv2.imread('bird1.jpg')

# writing img to computer
# cv2.imwrite(os.path.join( 'bird1_out.jpg'), img)

# visualoze
cv2.imshow('bird frame', img)

# to wait until i press a key
cv2.waitKey(0) # 0:- number of milliseconds opencv wantes to open the image
# 0 menas opncv opens window infinitly
#  if we commanded waitKey(0), opencv will opens the window and tehn close it immediatly

