class MyImage:
    def __init__(self, path):
        self.name = # basename without png
        self.path = #full path of image
        self.img = MyImage.load_img(path) #bgr from cv.imread
        self.label_ann = # 0 for carry, 1 for normal, 2 for threat
    
    def load_img(path):
