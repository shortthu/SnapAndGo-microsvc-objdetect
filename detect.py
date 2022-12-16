import cv2
import matplotlib.pyplot as plt
import torch
import random

class YoloV5_Detect:
    def __init__(self):
        self.model_detect = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        self.objects = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 
        'bus', 'train', 'truck', 'boat', 'traffic light', 
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 
        'cat', 'dog', 'horse', 'sheep', 'cow', 
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 
        'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 
        'wine glass', 'cup', 'fork', 'knife', 'spoon', 
        'bowl', 'banana', 'apple', 'sandwich', 'orange', 
        'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 
        'cake', 'chair', 'couch', 'potted plant', 'bed', 
        'dining table', 'toilet', 'tv', 'laptop', 'mouse', 
        'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 
        'toaster', 'sink', 'refrigerator', 'book', 'clock', 
        'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    def predict(self,img):
        # img = cv2.imread(image_src)
        detect = self.model_detect(img)
        regions = detect.xyxy[0]
        result = []
        for (x0,y0,x1,y1,score,label) in regions:
            object = {}
            object['object'] = self.objects[int(label)] 
            object['score'] = round(float(score) * 100, 2)
            object['coordinate'] = {'x0':int(x0), 'y0':int(y0), 'x1':int(x1), 'y1':int(y1)}
            result.append(object)

        return result
        # test sau
        # if len(detect.xyxy[0])==0: return None
        # coordinates = detect.xyxy[0][0]
        # coordinate = [int(coordinates[i]) for i in range(4)]
        # LpRegion = img[coordinate[1]:coordinate[3],coordinate[0]:coordinate[2]]
        # return LpRegion
