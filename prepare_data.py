import os
import seg
import get_pose as pose
from my_image import MyImage

# load img, seg, and pose and save an array of pickle files,
# save {'train': [MyImage0, MyImage1], 'val':[] , 'test':[a, b]}
to_pickle = {
    "train": [],
    "val": [],
    "test": []
    }

data_dir = "/home/t/tianqi/CS4243_proj/dataset/data"
for split in os.listdir(data_dir):
    print(split)
    subdir_path = os.path.join(data_dir, split)
    for label in os.listdir(subdir_path):
        split_path = os.path.join(subdir_path, label)
        for img in os.listdir(split_path):
            img_path = os.path.join(split_path, img)
            img_loaded = MyImage(img_path, label)
            to_pickle[split].append(img_loaded)
            
