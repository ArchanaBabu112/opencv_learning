import cv2
face_cascade= cv2.CascadeClassifier(r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Projects\opencv\haarcascades_haarcascade_frontalface_alt.xml")
webcam= cv2.VideoCapture(0)
while True:
    _, img= webcam.read()
    cv2.imshow("FACE DETECTION", img)
    key= cv2.waitkey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
