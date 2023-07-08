import torch
import numpy as np
import cv2
from time import perf_counter
from ultralytics import YOLO
import os
import yaml
from easydict import EasyDict as edict
from pathlib import Path

import supervision as sv
from bytettrack.byte_tracker import BYTETracker
from strongsort.strong_sort import StrongSORT

from util import YamlParser

SAVE_VIDEO = True
TRACKER = 'bytetrack'

