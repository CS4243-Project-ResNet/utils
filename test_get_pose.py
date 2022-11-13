from get_pose import get_pose_merge_s
# /home/t/tianqi/CS4243_proj/dataset/pose/carrying/A0194484R_20220903_carrying_11170.4411_200_keypoints.json
img_path = "/home/t/tianqi/CS4243_proj/dataset/splitted/train/carrying/A0194484R_20220903_carrying_11170.4411_200.png"
# img_path = "/home/t/tianqi/CS4243_proj/dataset/images/carrying/A0194513E_20220831_carrying_70900.58416_200.png"
# img_path = "/home/t/tianqi/CS4243_proj/dataset/splitted/train/carrying/A0194513E_20220831_carrying_02780.47469_30.png"
img_pose = get_pose_merge_s(img_path)
print(len(img_pose))
