import torch 
import torch.nn as nn 
from super_gradients.training import models

model_path = '/Users/arshad_221b/Downloads/Projects/YOLO/traffic/models/ckpt_best.pth'

model = models.get('yolo_nas_l',
                        num_classes=4,
                        checkpoint_path=model_path)

input_path = '/Users/arshad_221b/Downloads/Projects/YOLO/traffic/inputs/test6.mp4'
output_path = '/Users/arshad_221b/Downloads/Projects/YOLO/traffic/outputs/test6_output.mp4'

device = 0 if torch.cuda.is_available() else "cpu"


model.to(device).predict(input_path).save(output_path)