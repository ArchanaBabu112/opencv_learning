import os
import cv2

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\contour_bird.png"

img= cv2.imread(image_path)
# print(img.shape)

# when working iwth contours we are working with the borders of absolutely all isoluted white regions 
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh= cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
#  for conotur we are using grayscale img
contours, hierarchy=  cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>1: #to remove noise, by increasing values, some images are not fetching, they are considering as noises
        # cv2.drawContours(img, cnt, -1, (0,255,0), 1) #1: thickness, color :green
        x1, y1, w, h= cv2.boundingRect(cnt)
        # drwaing bounding boxes
        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0,255,0), 2) 


cv2.imshow("thresh", thresh)
cv2.imshow("img_gray", img)
cv2.waitKey(0)
