#!/bin/bash
# Install the libraries ....
apt-get update -y
apt-get install htop libgl1  wget unzip nano zip gcc htop tree -y
pip install gdown 

unzip yolov5.zip

# install rclone 
cd /root/
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip
unzip rclone-current-linux-amd64.zip
sudo cp rclone-v*-linux-amd64/rclone /usr/sbin/
rm -rf rclone-*

