import cv2

class Display():
    def __init__(self, img):
        self.disp(img)

    def disp(self, img):
        screen_res = 1280, 720
        scale_width = screen_res[0] / img.shape[1]
        scale_height = screen_res[1] / img.shape[0]
        scale = min(scale_width, scale_height)
        window_width = int(img.shape[1] * scale)
        window_height = int(img.shape[0] * scale)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', window_width, window_height)
        #cv2.rectangle(img, (x, y), (x2, y2), (0,0,255), 1)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()