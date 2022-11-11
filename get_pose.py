#return joint positions for the pose
import os.path as path
import json
import numpy as np

def get_pose(img_path):
    '''
    given an image path, read a respective pose json file from folder
    img_path: path of image of dataset/images/<class>/<image_name>.png
    assume pose json file is stored at dataset/pose/<class>/<image_name>.png
    return: a dictionary containing position of pose_keypoints_2d, hand_left_keypoints_2d and hand_right_keypoints_2d   
    '''
    img_basename = path.basename(img_path)
    img_name = path.splitext(img_basename)[0]
    img_dirname = path.dirname(img_path)
    imgs_dir, class_n = path.split(img_dirname)
    dataset_dir = path.dirname(imgs_dir[:-1])
    pose_basename = img_name + '_keypoints.json'
    pose_dir = path.join(dataset_dir, 'pose', class_n, pose_basename)

    f = open(pose_dir)
    pose_data = json.load(f)['people'][0]
    useless_info = ['person_id', 'face_keypoints_2d', 'pose_keypoints_3d', 'face_keypoints_3d', 'hand_left_keypoints_3d', 'hand_right_keypoints_3d']
    for w in useless_info:
        pose_data.pop(w)
    return pose_data

    
def get_pose_s(img_path):
    '''
    given an image path, read a respective pose json file from folder
    img_path: path of image of dataset/data/<test, train,val>/<class>/<image_name>.png
    assume pose json file is stored at dataset/pose/<class>/<image_name>.png
    return: a dictionary containing position of pose_keypoints_2d, hand_left_keypoints_2d and hand_right_keypoints_2d   
    '''
    img_basename = path.basename(img_path)
    img_name = path.splitext(img_basename)[0]
    img_dirname = path.dirname(img_path)
    imgs_dir, class_n = path.split(img_dirname)
    dataset_dir = path.dirname(imgs_dir[:-1])
    dataset_dir = path.dirname(dataset_dir[:-1])
    pose_basename = img_name + '_keypoints.json'
    pose_dir = path.join(dataset_dir, 'pose', class_n, pose_basename)

    f = open(pose_dir)
    pose_data = json.load(f)['people'][0]
    useless_info = ['person_id', 'face_keypoints_2d', 'pose_keypoints_3d', 'face_keypoints_3d', 'hand_left_keypoints_3d', 'hand_right_keypoints_3d']
    for w in useless_info:
        pose_data.pop(w)
    return pose_data

def get_pose_merge_s(img_path):
    '''
    given an image path, read a respective pose json file from folder
    img_path: path of image of dataset/data/<test, train,val>/<class>/<image_name>.png
    assume pose json file is stored at dataset/pose/<class>/<image_name>.png
    return: a dictionary containing position of pose_keypoints_2d, hand_left_keypoints_2d and hand_right_keypoints_2d   
    '''
    img_basename = path.basename(img_path)
    img_name = path.splitext(img_basename)[0]
    img_dirname = path.dirname(img_path)
    imgs_dir, class_n = path.split(img_dirname)
    dataset_dir = path.dirname(imgs_dir[:-1])
    dataset_dir = path.dirname(dataset_dir[:-1])
    pose_basename = img_name + '_keypoints.json'
    pose_dir = path.join(dataset_dir, 'pose', class_n, pose_basename)

    f = open(pose_dir)
    pose_data = json.load(f)['people'][0]
    useless_info = ['person_id', 'face_keypoints_2d', 'pose_keypoints_3d', 'face_keypoints_3d', 'hand_left_keypoints_3d', 'hand_right_keypoints_3d']
    for w in useless_info:
        pose_data.pop(w)
    pose_cat = []
    for key, value in pose_data.items():
        pose_cat += value
    return np.array(pose_cat)
