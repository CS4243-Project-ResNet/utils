import pickle as pkl

pkl_path = "/home/t/tianqi/CS4243_proj/nn_merge/20221110231334.pkl"

with open(pkl_path, "rb") as f:
    load = pkl.load(f)

print(load)
