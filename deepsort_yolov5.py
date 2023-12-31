import cv2
import numpy as np
import sys
import glob

import time 
import torch

class YoloDetector():

    def __init__(self, model_name):

        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print('Using Device: ', self.device)

    
    def load_model(self, model_name):

        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'custom', pretrained=True)
        return model

    def score_frame(self, frame):

        self.model.to(self.device)
        downscale_factor=2
        