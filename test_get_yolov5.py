from get_yolov5 import get_classifcation_bounding_box, get_classification

img_path = "/home/t/tianqi/CS4243_proj/dataset/images/carrying/A0194484R_20220903_carrying_11170.4411_200.png"
print(get_classifcation_bounding_box(img_path))
print(get_classification(img_path))
