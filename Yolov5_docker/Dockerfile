FROM ultralytics/yolov5:latest

RUN conda install -c conda-forge/label/cf202003 nodejs

RUN pip install -q tensorboard==2.2.1
RUN pip install -q jupyterlab jupyter_tensorboard ipywidgets


ENTRYPOINT ["jupyter","lab","--no-browser","--ip=0.0.0.0","--port=8888", "--allow-root"]

# docker build -t yolov5_jupyter .
# docker run --gpus all --shm-size 8G -p 8888:8888 -v $(pwd):/usr/src/app yolov5_jupyter