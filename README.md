# **Stero Matching PRO** 
![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

<div align="center">

![teaser](assets/teaser.png)

</div>

## **Table of Contents** 
- [**Environment setup**](#environment-setup)
- [**Data**](#data)
- [**Running**](#running)
- [**Reference**](#Reference)

## **Environment setup**
This code was tested with Python 3.8.3.
### Installation

```bash
git clone https://github.com/june65/StereoMatchingPro
pip install -r requirements.txt
```

## **Data**
Middlebury Computer Vision Pages provide datasets and benchmarks for computer vision research, including stereo vision, optical flow, and multi-view stereo. Download datasets at link [here](https://vision.middlebury.edu/stereo/data/scenes2001/). 


## **Running**
### Absolute intensity difference
```bash
python main.py --costmethod AD
```

<div style="display: flex; justify-content: center;">
    <img src="assets/AD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/AD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

### Squared intensity difference
```bash
python main.py --costmethod SD
```

<div style="display: flex; justify-content: center;">
    <img src="assets/SD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>


### Sum of absolute differences
```bash
python main.py --costmethod SAD
```

<div style="display: flex; justify-content: center;">
    <img src="assets/SAD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SAD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

### Sum of squared differences
```bash
python main.py --costmethod SSD
```

<div style="display: flex; justify-content: center;">
    <img src="assets/SSD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SSD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

### Adaptive Support Weights
```bash
python main.py --costmethod ASW
```

<div style="display: flex; justify-content: center;">
    <img src="assets/ASW_left_disparity_33.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/ASW_right_disparity_33.png" alt="Image 2" style="height: 200px;"/>
</div>

### Semi-Global Matching
```bash
python main.py --costmethod SGM
```

<div style="display: flex; justify-content: center;">
    <img src="assets/SGM_aggregated_volume.png" alt="Image 1" style="height: 200px;"/>
</div>

### Left Right Consistency Check
```bash
python main.py --costmethod SAD --lrcheck True
```

<div style="display: flex; justify-content: center;">
    <img src="assets/LR_check_SAD_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

### Weighted Median Filter
```bash
python main.py --costmethod ASW --midfilter True
```

<div style="display: flex; justify-content: center;">
    <img src="assets/Mid_filter_ASW_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

## **Reference**
[Stereo Matching With Fusing Adaptive Support Weights](https://ieeexplore.ieee.org/document/8712528)

[Stereo Processing by Semi-Global Matching and Mutual Information](https://core.ac.uk/download/pdf/11134866.pdf)













