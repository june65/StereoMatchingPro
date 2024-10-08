# **Stereo Matching PRO** ![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

Dive into the world of computer vision with this comprehensive Python project that brings stereo matching to life. Designed for enthusiasts and professionals alike, this project leverages cutting-edge algorithms to generate precise depth maps from stereo image pairs. Whether you're exploring autonomous systems, 3D reconstruction, or just expanding your knowledge, this project offers a hands-on approach to mastering stereo vision.

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

We demonstrate the precision of our stereo matching algorithms using the benchmark Tsukuba dataset.

### Ground Truth

<div style="display: flex; justify-content: center;">
    <img src="assets/Ground_Truth.png" alt="Image 1" style="height: 200px;"/>
</div>

### Absolute intensity difference
```bash
python main.py --costmethod AD --rgbexpand True
```
![RMSE](https://img.shields.io/badge/RMSE-3.472-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.393-red)
<div style="display: flex; justify-content: center;">
    <img src="assets/AD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/AD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

### Squared intensity difference
```bash
python main.py --costmethod SD --rgbexpand True
```
![RMSE](https://img.shields.io/badge/RMSE-3.174-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.381-red)
<div style="display: flex; justify-content: center;">
    <img src="assets/SD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

### Sum of absolute differences
```bash
python main.py --costmethod SAD --costwindow 3
```
<div style="display: flex; justify-content: center;">
    <img src="assets/SAD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SAD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

```bash
python test.py --costmethod SAD --costwindow 33
```
![RMSE](https://img.shields.io/badge/RMSE-1.975-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.115-red)

<div style="display: flex; justify-content: center;">
    <img src="assets/SAD_accuracy_window_size.png" alt="Image 1" style="height: 300px;"/>
</div>

### Sum of squared differences
```bash
python main.py --costmethod SSD --costwindow 3
```
<div style="display: flex; justify-content: center;">
    <img src="assets/SSD_left_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/SSD_right_disparity.png" alt="Image 2" style="height: 200px;"/>
</div>

```bash
python test.py --costmethod SSD --costwindow 33
```
![RMSE](https://img.shields.io/badge/RMSE-1.958-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.125-red)

<div style="display: flex; justify-content: center;">
    <img src="assets/SSD_accuracy_window_size.png" alt="Image 1" style="height: 300px;"/>
</div>

### Adaptive Support Weights
```bash
python main.py --costmethod ASW --costwindow 33
```

<div style="display: flex; justify-content: center;">
    <img src="assets/ASW_left_disparity_33.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/ASW_right_disparity_33.png" alt="Image 2" style="height: 200px;"/>
</div>

```bash
python test.py --costmethod ASW --costwindow 51
```
![RMSE](https://img.shields.io/badge/RMSE-2.043-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.108-red)

<div style="display: flex; justify-content: center;">
    <img src="assets/AWS_accuracy_window_size.png" alt="Image 1" style="height: 300px;"/>
</div>

### Semi-Global Matching
```bash
python main.py --costmethod SGM
```

<div style="display: flex; justify-content: center;">
    <img src="assets/SGM_aggregated_volume.png" alt="Image 1" style="height: 200px;"/>
</div>

### Graph Cut
```bash
python main.py --costmethod AD --graphcut True
```
![RMSE](https://img.shields.io/badge/RMSE-2.083-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.135-red)
<div style="display: flex; justify-content: center;">
    <img src="assets/AD_Graph_cut_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

### Left Right Consistency Check
```bash
python main.py --costmethod SAD --costwindow 3 --lrcheck True
```

<div style="display: flex; justify-content: center;">
    <img src="assets/LR_check_SAD_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

### Tree Filtering
```bash
python main.py --costmethod ASW --costwindow 27 --treefilter True --lrcheck True
```
![RMSE](https://img.shields.io/badge/RMSE-2.073-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.102-red)

<div style="display: flex; justify-content: center;">
    <img src="assets/Tree_filter_LR_check_ASW_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
    <img src="assets/Tree_filter_MST.png" alt="Image 1" style="height: 200px;"/>
</div>

### Weighted Median Filter
```bash
python main.py --costmethod ASW --costwindow 33 --midfilter 5
```
![RMSE](https://img.shields.io/badge/RMSE-2.023-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.106-red)

<div style="display: flex; justify-content: center;">
    <img src="assets/Mid_filter_ASW_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

### Best Result
ASW + Left Right Consistency Check + Tree Filtering + Weighted Median Filter
```bash
python main.py --costmethod ASW --costwindow 33 --lrcheck True --treefilter True --midfilter 5 
```
![RMSE](https://img.shields.io/badge/RMSE-2.039-brightgreen)
![Bad Ratio](https://img.shields.io/badge/Bad%20Ratio-0.102-red)
<div style="display: flex; justify-content: center;">
    <img src="assets/Mid_filter_Tree_filter_LR_check_ASW_aggregated_disparity.png" alt="Image 1" style="height: 200px;"/>
</div>

## **Reference**
[Stereo Matching With Fusing Adaptive Support Weights](https://ieeexplore.ieee.org/document/8712528)

[Stereo Processing by Semi-Global Matching and Mutual Information](https://core.ac.uk/download/pdf/11134866.pdf)

[Stereo Matching Using Tree Filtering](https://ieeexplore.ieee.org/abstract/document/6888475)

[Constant Time Weighted Median Filtering for Stereo Matching](https://openaccess.thecvf.com/content_iccv_2013/papers/Ma_Constant_Time_Weighted_2013_ICCV_paper.pdf)










