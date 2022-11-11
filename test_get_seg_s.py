import cv2 as cv
import seg

img_path = "/home/t/tianqi/CS4243_proj/dataset/splitted/train/carrying/A0194484R_20220903_carrying_11170.4411_200.png"
img = cv.imread(img_path)
save_dir = "/home/t/tianqi/CS4243_proj/PP-HumanSeg/img_trial/out/A0194484R_20220903_carrying_11170.4411_200_2.png"

# arr is 2d
def show_arr(arr):
    for row in range(arr.shape[0]):
        row_str = ""
        for col in range(arr.shape[1]):
            row_str += " {}".format(arr[row, col])
        print(row_str)

seg_int = seg.get_seg_int_split(img_path)
show_arr(seg_int)
seg_f = seg.get_seg_f_s(img_path)
show_arr(seg_f)
seg_bin = seg.get_seg_bin_s(img_path)
show_arr(seg_bin)
masked_img = seg.get_seg_masked_s(img, img_path, 50)

cv.imwrite(save_dir, masked_img)
