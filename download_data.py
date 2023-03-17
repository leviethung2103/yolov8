import yaml
import gdown
import re
import zipfile
import os 

DATASET_FOLDER = "datasets"

def unzip_file(file_path, extract_to):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

def get_drive_id(url):
    file_id_match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)

    if file_id_match:
        file_id = file_id_match.group(1)
    return file_id

# Open the YAML file and load it into a dictionary
with open('dataset.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

# Dataset 1 
output = "License-Plate-ChienKhuong-LPR.zip"
id = get_drive_id(data['License-Plate-ChienKhuong-LPR'])
gdown.download(id=id, output=os.path.join(DATASET_FOLDER, output), quiet=False)

unzip_file(os.path.join(DATASET_FOLDER, output), DATASET_FOLDER)




