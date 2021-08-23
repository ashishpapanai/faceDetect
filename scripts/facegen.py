import matplotlib.pyplot as plt
from mtcnn import MTCNN
import datetime

class faceGen():
    def __init__(self, img, result_list):
        self.faces(img, result_list)
    
    def faces(self, img, result_list):
        data = img[:,:,::-1] # RGB to BGR
        #result_list = MTCNN().detect_faces(data)
        for i in range(len(result_list)):
            x1, y1, width, height = result_list[i]['box']
            x2, y2 = x1 + width, y1 + height
            #plt.plot(1, len(result_list), i)
            plt.axis('off')
            # plot face
            plt.imshow(data[y1:y2, x1:x2])
            plt.subplots_adjust(bottom=0, top=1, left=0, right=1)
            plt.savefig('./faceGen/face'+"_"+str(datetime.datetime.now().date())+"_"+str(datetime.datetime.now().strftime("%H-%M-%S"))+"_"+str(i)  +'.png')
        # show the plot
        #plt.show()