import cv2 as cv
import os
from PIL import Image

import seg
import get_pose as pose

class_dict = {
    "carrying": 0,
    "normal": 1,
    "threat": 2
}

class MyImage:
    def __init__(self, path, label, seg_thres=50):
        self.name = path.basename(path) # basename without png
        self.path = path #full path of image
        self.img = MyImage.load_img(path) #bgr from cv.imread
        self.c_id = class_dict[label] # 0 for carry, 1 for normal, 2 for threat
        self.seg_bin = seg.get_seg_bin_s(path)
        self.seg_masked = seg.get_seg_masked_s(path, seg_thres) #masked seg image
        self.pose = pose.get_pose
    
    def load_img(path):
        Image.open(path)

    def update_seg_thres(self, thres):
        self.seg_masked = seg.get_seg_masked_s(self.path, thres)
