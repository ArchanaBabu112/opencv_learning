#  everytime we applyig blur we are applyig averging, 
#  we are replacing that part with the average value of all the pixels in the neighbourhood of that pixel
#  the way we choosisng the nightboour, (size of the neighbour, deplends on the bluring mehtod we are usig

import os, cv2

image_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\images\bird1.jpg"

img= cv2.imread(image_path)

k_size= 7 #larger this number , stronger theblur
# img_blur= cv2.blur(img, (k_size, k_size))

median_blur= cv2.medianBlur(img, k_size)

# gauss_blur= cv2.GaussianBlur(img, (k_size, k_size), 3)
cv2.imshow("blur_img", median_blur)
cv2.waitKey(0)


# Bluring are of 4 types:
# blur, gaussina_blur, media_blur, bilateral blur

