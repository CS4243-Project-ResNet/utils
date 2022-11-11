# utils
## Dataset Folder Structure with Augmentation:
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
## Seg Threshold