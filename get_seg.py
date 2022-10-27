import os.path as path
import cv2 as cv

def get_seg(img_path):
    '''
    read segmentation mask from folder
    img_path: path of image of dataset/images/<class>/<image_name>.png
    assume segmentation mask is stored at dataset/seg/<class>/<image_name>.png
    return: gray level np.uint8 [0, 255] with image.shape
    '''
    img_basename = path.basename(img_path)
    img_dirname = path.dirname(img_path)
    images_dir, class_n = path.split(image_dirname[:-1])
    dataset_dir = path.dirname(image_dir[:-1])
    seg_dir = path.join(dataset_dir, 'seg', class_n, image_basename)
    return cv.imread(seg_dir, 0)

def get_seg_float(img_path):
    '''
    return: [0, 1] image of seg mask with image.shape
    '''
    return get_seg(image_path) / 256

def seg_mask_binary(img_path, thres=10):
    '''
    thres: value < thres considered 0
    use cv.bitwise_and to
    return: binary mask of thresed seg
    '''
    seg = get_seg(img_path)
    thred = cv.threshold(seg, thres, 255, cv.THRESH_BINARY)
    return thred

def get_img_masked(img, image_path, thres=10):
    '''
    return: masked image
    '''
    return cv.bitwise_and(img, img, mask = seg_mask_binary(image_path, thres))
