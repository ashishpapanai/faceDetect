import cv2
from mtcnn import MTCNN
import display, facegen


img = (cv2.imread("images/test3.jpg"))
img = cv2.resize(img, (600, 600), interpolation = cv2.INTER_NEAREST)
display.Display(img)
detector  = MTCNN()
faces = detector.detect_faces(img)

for i in range(0, len(faces)):
    result = faces[i]
    x, y, width, height = result['box']
    x2 = x + width
    y2 = y + height
    img = cv2.rectangle(img, (x, y), (x2, y2), (0,0,255), 1)
    # create the shape
    for key, value in result['keypoints'].items():
			# create and draw dot
            img = cv2.circle(img, value, radius=2, color=(0,0,255))
            
#display.Display(img)
facegen.faceGen(img, faces)