import os, cv2
import numpy as np

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\whiteboard2.jpg"

img= cv2.imread(image_path)
print(img.shape)
# line
# cv2.line(img,  (60,95), (7,125),(0,255,0), 6)#starting and end points


# rectangle

# cv2.rectangle(img, (60,95), (7,125), (0,0,255), 6) #instead of 6 if we chose -1, the rectalge will be completed filled, means completed oclored. 6 determines the thickness.

# circle
cv2.circle(img, (100, 150), 15, (255,0,0),10) # 15;- radius, (100,150):- centre, (255,0,0):- blue color, 15:- thickness

# text
cv2.putText(img, 'Hey you!', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
