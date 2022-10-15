import cv2 as cv
import os
from os import listdir

folder_dir = "/home/tz/CS4243_proj/cs4243_smallest/carrying"
for image in os.listdir(folder_dir):
    # check if the image ends with png
    if (image.endswith(".png")):
        # print(image)
        img_dir = os.path.join(folder_dir, image)
        img_cv = cv.imread(img_dir)
        print(img_cv.shape)