# YOLO-NAS object detection on custom dataset 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is centered around a YOLO-NAS (You Only Look One - Neural Architecture Search) object detection model. It offers a comprehensive guide for building and training a custom YOLO-NAS model tailored to detect specific objects. In this instance, the model is trained to recognize street signs and classify them into four categories.

## DEMO
<div align='center'>
  
![](demo/ezgif.com-video-to-gif.gif)

</div>

## Training and Validation 
Utilize the traffic.ipynb notebook for training and validating the custom model. This notebook, originally crafted by AarohiSingla for fall detection, requires Python 3.9 or higher.


## Inference 
Once trained, the model is ready for use with the flask_app. The flask_app folder contains app.py, allowing users to upload images or videos for object detection. Configure settings in the config folder. 

## References and Datasets 
1) Original Code built for fall detection: https://github.com/AarohiSingla
2) Dataset for traffic sign detection: https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format
3) YOLO-NAS: https://learnopencv.com/yolo-nas/
4) Video demo: https://www.youtube.com/watch?v=40xZVEFVBuE
