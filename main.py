import cv2
from mtcnn import MTCNN
import display
img = (cv2.imread("images/test3.jpg"))
img = cv2.resize(img, (1280, 720), interpolation = cv2.INTER_NEAREST)



detector  = MTCNN()
faces = detector.detect_faces(img)

for i in range(0, len(faces)):
    x, y, width, height = faces[i]['box']
    x2 = x + width
    y2 = y + height
    # create the shape
    img = cv2.rectangle(img, (x, y), (x2, y2), (0,0,255), 1)

display.Display(img)