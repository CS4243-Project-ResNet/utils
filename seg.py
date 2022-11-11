import os.path as path
import cv2 as cv

def get_seg_int(img_path):
    '''
    read segmentation mask from folder
    img_path: path of image of dataset/images/<class>/<image_name>.png
    assume segmentation mask is stored at dataset/seg/<class>/<image_name>.png
    return: gray level np.uint8 [0, 255] with image.shape
    '''
    img_basename = path.basename(img_path)
    img_dirname = path.dirname(img_path)
    # print(img_dirname)
    imgs_dir, class_n = path.split(img_dirname)
    # print(imgs_dir)
    # print(class_n)
    dataset_dir = path.dirname(imgs_dir[:-1])
    seg_dir = path.join(dataset_dir, 'seg', class_n, img_basename)
    # print(seg_dir)
    im_read = cv.imread(seg_dir, 0)
    return im_read

def get_seg_f(img_path):
    '''
    return: [0, 1] image of seg mask with image.shape
    '''
    return get_seg_int(img_path) / 255

def get_seg_bin(img_path, thres=50):
    '''
    thres: value < thres considered 0
    use cv.bitwise_and to
    return: binary mask of thresed seg
    '''
    seg = get_seg_int(img_path)
    ret, mask = cv.threshold(seg, thres, 1, cv.THRESH_BINARY)
    return mask

def get_seg_masked(img, img_path, thres=50):
    '''
    return: masked image
    '''
    return cv.bitwise_and(img, img, mask = get_seg_bin(img_path, thres))

def get_seg_int_split(img_path):
    '''
    read segmentation mask from folder
    img_path: path of image of dataset/images/<train,val,test>/<class>/<image_name>.png
    assume segmentation mask is stored at dataset/seg/<class>/<image_name>.png
    return: gray level np.uint8 [0, 255] with image.shape
    '''
    print(img_path)
    img_basename = path.basename(img_path)
    img_dirname = path.dirname(img_path)
    # print(img_dirname)
    imgs_dir, class_n = path.split(img_dirname)
    # print(imgs_dir)
    # print(class_n)
    dataset_dir = path.dirname(imgs_dir[:-1])
    dataset_dir = path.dirname(dataset_dir[:-1])
    seg_dir = path.join(dataset_dir, 'seg', class_n, img_basename)
    # print(seg_dir)
    im_read = cv.imread(seg_dir, 0)
    return im_read

def get_seg_f_s(img_path):
    '''
    return: [0, 1] image of seg mask with image.shape
    '''
    return get_seg_int_split(img_path) / 255

def get_seg_bin_s(img_path, thres=50):
    '''
    thres: value < thres considered 0
    use cv.bitwise_and to
    return: binary mask of thresed seg
    '''
    seg = get_seg_int_split(img_path)
    ret, mask = cv.threshold(seg, thres, 255, cv.THRESH_BINARY)
    return mask

def get_seg_masked_s(img, img_path, thres=50):
    '''
    return: masked image
    '''
    return cv.bitwise_and(img, img, mask = get_seg_bin_s(img_path, thres))

