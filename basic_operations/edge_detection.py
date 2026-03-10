import os, cv2
import numpy as np

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\bird1.jpg"

img= cv2.imread(image_path)

img_edge= cv2.Canny(img, 100, 200)

img_edge_d= cv2.dilate(img_edge, np.ones((2,2), dtype=np.int8))
# opposite action of dilate is erode, dilate higlights the edges
img_edge_e= cv2.erode(img_edge_d, np.ones((2,2), dtype=np.int8))

cv2.imshow("img", img)
cv2.imshow("img_edge_e", img_edge_e)

cv2.imshow("img_edge_d", img_edge_d)
cv2.waitKey(0)