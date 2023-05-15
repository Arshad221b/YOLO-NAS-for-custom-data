# YOLO-NAS object detection on custom dataset 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A project that is built on a YOLO-NAS object detection model. This project provides a flow to build and train a custom YOLO-NAS model for custom objects. In this particular case the model is trained to detect signs on the street and classify them into four categories. 

## DEMO
<div align='center'>
  
![](demo/ezgif.com-video-to-gif.gif)

</div>

## Training and Validation 
Use traffic.ipynb to train and and validate custom model. 

This notebook was originally built by https://github.com/AarohiSingla for fall detection


## Inference 
After training, model is ready to use with flask_app. The folder flask_app contains app.py. User can upload images or videos to for object detection. Set config in the config folder. 

## References and Datasets 
1) Original Code built for fall detection: https://github.com/AarohiSingla
2) Dataset for traffic sign detection: https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format
3) YOLO-NAS: https://learnopencv.com/yolo-nas/
4) Video for demo: https://www.youtube.com/watch?v=40xZVEFVBuE
