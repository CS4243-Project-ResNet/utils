import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/t/tianqi/CS4243_proj/utils/best_11_09.pt')
model.conf = 0.1

def get_classification(file_path):
    '''
    Classification
    -1: None
    0: gun
    1: knife
    '''
    results = model(file_path, size=540)

    if len(results.xyxy[0]) == 0:
        return -1
    else:
        return int(results.xyxy[0][0][5])

def get_classifcation_bounding_box(file_path):
    results = model(file_path, size=540)

    objects = []
    for obj in results.xyxy[0]:
        objects.append(
            {
                "class": int(obj[5]), 
                "xmin": float(obj[0]),
                "ymin": float(obj[1]),
                "xmax": float(obj[2]),
                "ymax": float(obj[3]),
            })
    return objects
