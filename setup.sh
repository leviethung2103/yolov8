#!/bin/bash
# Install the libraries ....
apt-get update 
apt-get install htop libgl1
pip install gdown nano
apt-get install -y wget; wget https://raw.githubusercontent.com/vast-ai/vast-python/master/vast.py -O vast; chmod +x vast;∆