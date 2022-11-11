import datetime as dt
import pickle as pkl
import os

to_pickle = []

save_dir = "/home/t/tianqi/CS4243_proj/nn_merge"
curr_time = dt.datetime.now().strftime("%Y%m%d%H%M%S")
save_basename= curr_time + ".pkl"
save_path = os.path.join(save_dir, save_basename)
print(save_path)

with open(save_path, 'wb') as fp:
    pkl.dump(to_pickle, fp)

