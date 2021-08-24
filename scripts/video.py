# source:  https://realpython.com/face-detection-in-python-using-a-webcam/
import cv2
import sys
cascPath = sys.argv[0] #path of current folder
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # Load the cascade classifier
video_capture = cv2.VideoCapture(0) # selects default webcam
while True:
    ret, frame = video_capture.read() # reads frame from webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts frame to grayscale
    faces = faceCascade.detectMultiScale( # detects faces in frame
        gray, # grayscale frame
        scaleFactor=1.1, # scale factor for image
        minNeighbors=5, # minimum number of neighbors
        minSize=(30, 30), # minimum size of face
        flags=cv2.CASCADE_SCALE_IMAGE # flags
    )
    for (x, y, w, h) in faces: # draws rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1)& 0xFF == ord('q'): # waits till user presses q
        break
video_capture.release() # releases webcam
cv2.destroyAllWindows() # destroys all windows