import cv2 as cv
import os
from PIL import Image

import seg
import get_pose as pose
import get_yolov5 as weapon

class_dict = {
    "carrying": 0,
    "normal": 1,
    "threat": 2
}

class MyImage:
    def __init__(self, img_path, label, seg_thres=50):
        self.name = os.path.basename(img_path) # basename without png
        self.img_path = img_path #full img_path of image
        self.img = MyImage.load_img(img_path) #bgr from cv.imread
        self.c_id = class_dict[label] # 0 for carry, 1 for normal, 2 for threat
        self.seg_bin = seg.get_seg_bin_s(img_path)
        self.seg_masked = seg.get_seg_masked_s(img_path, seg_thres) #masked seg image
        self.pose = pose.get_pose # 
        self.weapon_r = weapon.get_classifcation_bounding_box(img_path) #
        self.weapon_c = weapon.get_classification(img_path)
    
    def load_img(img_path):
        Image.open(img_path)

    def update_seg_thres(self, thres):
        self.seg_masked = seg.get_seg_masked_s(self.img_path, thres)

    def __repr__(self):
        return "({},{})".format(self.name, self.c_id)

    def display_pose(self):
        print(self.pose)

    def display_weapon(self):
        print(self.weapon_r)
        print(self.weapon_c)
