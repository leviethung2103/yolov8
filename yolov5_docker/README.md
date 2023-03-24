## Yolov5 - Jupyter Lab - For Training
Used to deploy on local machine

Based on `ultralytics/yolov5`, I added Jupyter Lab


## Steps
1. Build docker image
```bash
docker build -t yolov5_jupyter .
```

2. Start the container
```bash
docker run --gpus all --shm-size 8G -p 8888:8888 -v $(pwd):/usr/src/app yolov5_jupyter
```


# Check PyTorch Automatic Mixed Precision (AMP) functionality. Return True on correct operation
Nếu gặp lỗi loss =nan thì sửa trong file train.py amp = False

AMP: Mixed Precision: Train ít tốn bộ nhớ GPU hơn. 