import os
import cv2

# video_path= r"C:\Users\464_0863\OneDrive - Yokogawa Electric Corporation\Attachments\Projects\opencv\videos"
video_path= os.path.join('.', 'videos', '18432483-hd_1080_1920_30fps.mp4')
video= cv2. VideoCapture(video_path)

#  visualization video

cv2. namedWindow("video_frame", cv2.WINDOW_NORMAL)
ret= True
while ret:
    ret, frame=video.read()
    #  ret to ensure we are reading all the frames
    #  ret is aboolean value tha twill be true each time we successfully read a fram e, and will befale when a new frame is not read

    resized_frame= cv2.resize(frame, (800, 600))
    cv2.imshow('video_frame', resized_frame)

    cv2.waitKey(10) & 0xFF==ord('q')
    #  if the window is closed, detecting closed window
    if cv2.getWindowProperty("video_frame", cv2.WND_PROP_VISIBLE)<1:
        break
    
    # If the user presses the q key, stop the loop., q is the ASCII number q=113
    #  wait 40 millisecond on each frame before showing the next frame 
video.release() # opencv releasing th ememory allocated to this window
cv2.destroyAllWindows()

