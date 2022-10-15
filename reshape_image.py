import cv2 as cv
import os
from os import listdir

read_dir = "/home/tz/CS4243_proj/cs4243_smallest"
write_dir = "/home/tz/CS4243_proj/cs4243_smallest_reshaped"

re_shape= (192, 192)

for image in os.listdir(read_dir):
    
    # check if the image ends with png
    if (image.endswith(".png")):
        img_dir = os.path.join(read_dir, image)
        img_cv = cv.imread(img_dir)
        print(img_cv.shape)
        reshaped = cv.resize(img_cv, re_shape)
        save_dir = os.join(write_dir, image)
        cv.imwrite(save_dir, reshaped)