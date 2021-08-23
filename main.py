import cv2
from mtcnn import MTCNN
import display
img = (cv2.imread("images/test2.jpg"))
#img = cv2.resize(img, (780, 540), interpolation = cv2.INTER_NEAREST)



'''detector  = MTCNN()
faces = detector.detect_faces(img)
box = result[0]['box']
x, y, width, height = box
x2, y2 = x + width, y + height
print(box)'''