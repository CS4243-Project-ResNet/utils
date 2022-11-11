# memory error

import datetime as dt
import os
import pickle as pkl

from my_image import MyImage

# load img, seg, and pose and save an array of pickle files,
# save {'train': [MyImage0, MyImage1], 'val':[] , 'test':[a, b]}
to_pickle = {
    "train": [],
    "val": [],
    "test": []
    }


data_dir = "/home/t/tianqi/CS4243_proj/dataset/splitted"
for split in os.listdir(data_dir):
    print(split)
    subdir_path = os.path.join(data_dir, split)
    for label in os.listdir(subdir_path):
        print(label)
        split_path = os.path.join(subdir_path, label)
        for img in os.listdir(split_path):
            img_path = os.path.join(split_path, img)
            print(img_path)
            img_loaded = MyImage(img_path, label)
            to_pickle[split].append(img_loaded)

save_dir = "/home/t/tianqi/CS4243_proj/nn_merge"
curr_time = dt.datetime.now().strftime("%Y%m%d%H%M%S")
save_basename= curr_time + ".pkl"
save_path = os.path.join(save_dir, save_basename)

with save_path.open('wb') as fp:
    pkl.dump(to_pickle, fp)

