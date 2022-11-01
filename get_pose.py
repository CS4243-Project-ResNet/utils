#return joint positions for the pose
import os.path as path
import json

def get_pose(img_path):
    '''
    given an image path, read a respective pose json file from folder
    img_path: path of image of dataset/images/<class>/<image_name>.png
    assume pose json file is stored at dataset/pose/<class>/<image_name>.png
    return: #TODO 
    '''
    img_basename = path.basename(img_path)
    img_name = path.splitext(img_basename)[0]
    print(img_name)
    img_dirname = path.dirname(img_path)
    print(img_dirname) 
    imgs_dir, class_n = path.split(img_dirname)
    print(imgs_dir) 
    print(class_n) 
    dataset_dir = path.dirname(imgs_dir[:-1])
    print(dataset_dir) 
    pose_basename = img_name + '.json'
    pose_dir = path.join(dataset_dir, 'pose', class_n, pose_basename)
    print(pose_dir) 

    f = open(pose_dir)
    pose_data = json.load(f)['people'][0]
    useless_info = ['person_id', 'face_keypoints_2d', 'pose_keypoints_3d', 'face_keypoints_3d', 'hand_left_keypoints_3d', 'hand_right_keypoints_3d']
    for w in useless_info:
        pose_data.pop(w)
    return pose_data

    
