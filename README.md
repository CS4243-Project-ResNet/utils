# How to run our code
## Preprocessing
### PP-HumanSeg
- install [PaddlePaddle](https://github.com/PaddlePaddle/Paddle)
- pull paddleseg [repo](https://github.com/PaddlePaddle/PaddleSeg)
- follow instruction in [PP-HumanSeg](https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.6/contrib/PP-HumanSeg)
### OpenPose
- pull OpenPose [repo](https://github.com/CMU-Perceptual-Computing-Lab/openpose.git)
- follow instruction in [instruction](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/README.md) (run with parameter --hand)
### yolov5
- pull yolov5 [repo](https://github.com/ultralytics/yolov5)
- run hyperparameter evolution
- train with evolved hyperparameter
## Dataset Folder Structure with Augmentation (For pose mlp and merge):
```
dataset/
|--images/
    |--train
    |  |--carry/
    |  |--normal/
    |  |--threat
    |--val
    ...
|--pose/
|  |--carry/<image_name>.json
|  |--normal/
|  |--threat/
|--seg/ 
|  |--carry/<image_name>.png
|  |  ...
|   
|--my_utils/
   |--xxx.py
|--nn_merge/
   |--xx.py
```
## Code folder structure
```
CS4243_proj/
|--dataset/(same as above)
|--baseline/
   |--data/
      |--train/carrying
      |...
   |seg
      |--train/carrying
      ...
   |--<baseline resnet>.py/ipynb
   |--<seg with resnet>.py/ipynb
|--nn_merge/
   |--merge_mlp_<number>.py --> final combination for mlp training
   |--my_dataset_1.py --> dataset and dataloader definition
   |--linear_combination.py
|--my_utils/ --> util files (abstraction for preprocessing)

```
