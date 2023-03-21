## Train Object Detection with Yolov8

## Download dataset
Unzip the dataset zip file and place inside `datasets` folder

## Convert CVAT -> YOLO
1.Create_Dataset_From_Yolo
Download dataset from CVAT as Yolo 1.0 Annotation Format
Run the script
- Split into `images` and `labels` folders 
- Create `data.yml` file 
- Split train, val, test by ratio 80:10:10
- Statistic on dataset

## Setup
Install the packages
```
chmod +x setup.sh
./setup.sh
```
Download the `dataset.yml` and place it at the root directory
```
python download_data.py
```
