# %%
# create the classes
import yaml
import os 
import shutil
from datetime import datetime
import pandas as pd
import random


now = datetime.now()
current_time = now.strftime("%d-%m-%Y")


# Update Parameters Here
VERSION = "v1.0"
TASKNAME = "LPD" # LPD or LPR
INPUT_IMAGE = "/media/hunglv/T7/lpd_lao_chienkhuong_21022023_3000_v1.0/obj_train_data/ChienKhuong_21_02_2023_3k"
INPUT_OBJ_NAME = "/media/hunglv/T7/lpd_lao_chienkhuong_21022023_3000_v1.0/obj.names"
TARGET_NAME = "LAO_ChienKhuong"

train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# OUTPUT 
OUTPUT_DATASET = f"{TASKNAME}_{TARGET_NAME}_{current_time}_{VERSION}"

if not os.path.exists(OUTPUT_DATASET):
    os.makedirs(OUTPUT_DATASET)

def make_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

def split_files(directory, output_directory):
    """
    This function takes a directory path and splits files with extensions .jpg and .png into an 'images' folder, 
    and files with extension .txt into a 'labels' folder.
    """
    train_images_dir = os.path.join(output_directory, "train", 'images')
    train_labels_dir = os.path.join(output_directory, "train", 'labels')
    
    val_images_dir = os.path.join(output_directory, "val", 'images')
    val_labels_dir = os.path.join(output_directory, "val", 'labels')
    
    test_images_dir = os.path.join(output_directory, "test", 'images')
    test_labels_dir = os.path.join(output_directory, "test", 'labels')
    
    assert len(os.listdir(directory)) != 0 

    # Create the 'images' and 'labels' folders if it doesn't exist
    make_folder(train_images_dir)
    make_folder(train_labels_dir)
    make_folder(val_images_dir)
    make_folder(val_labels_dir)
    make_folder(test_images_dir)
    make_folder(test_labels_dir)
    
    all_files = os.listdir(directory)
    
    random.shuffle(all_files)
    
    # calculate the number of images in each set
    num_train_files = int(len(all_files) * train_ratio)
    num_val_files = int(len(all_files) * val_ratio)
    num_test_files = int(len(all_files) * test_ratio)
    
    # split the files into sets
    train_data = all_files[:num_train_files]
    val_data = all_files[num_train_files:num_train_files+num_val_files]
    test_data = all_files[num_train_files+num_val_files:]
    
    data = []
    
    # Loop through all files in directory and move to appropriate folder based on extension
    for filename in train_data:
        if not filename.startswith("."):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                basename = os.path.splitext(filename)[0]
                data += [dict(filename = basename, has_label = os.path.getsize(os.path.join(directory, basename + ".txt")) > 0)]
                # move image
                shutil.move(os.path.join(directory, filename), train_images_dir) 
                # move label
                shutil.move(os.path.join(directory, basename + ".txt"), train_labels_dir) 
                

    for filename in val_data:
        if not filename.startswith("."):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                basename = os.path.splitext(filename)[0]
                data += [dict(filename = basename, has_label = os.path.getsize(os.path.join(directory, basename + ".txt")) > 0)]
                # move image
                shutil.move(os.path.join(directory, filename), val_images_dir) 
                # move label
                shutil.move(os.path.join(directory, basename + ".txt"), val_labels_dir) 
                
    for filename in test_data:
        if not filename.startswith("."):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                basename = os.path.splitext(filename)[0]
                data += [dict(filename = basename, has_label = os.path.getsize(os.path.join(directory, basename + ".txt")) > 0)]
                # move image
                shutil.move(os.path.join(directory, filename), test_images_dir) 
                # move label
                shutil.move(os.path.join(directory, basename + ".txt"), test_labels_dir) 

    return pd.DataFrame(data)

def write_yaml(output_dir):
    with open(INPUT_OBJ_NAME, "r") as file:
        classes = file.readlines()
        classes = [item.strip() for item in classes]

    data = {
        "names": classes, 
        "nc": len(classes),
        'roboflow': {
            'license': 'Private',
            'project': 'license-plate-fti9n',
            'url': 'https://app.roboflow.com/hungle/license-plate-fti9n/1',
            'version': 1,
            'workspace': 'hungle'
        },
        'test': os.path.join(OUTPUT_DATASET,"test","images"),
        'train': os.path.join(OUTPUT_DATASET,"train","images"),
        'val': os.path.join(OUTPUT_DATASET,"val","images")
    }

    # Save dictionary as YAML file
    with open(os.path.join(output_dir,'data.yaml'), 'w') as file:
        yaml.dump(data, file)
        
def save_df(OUTPUT_DATASET,df):
    df.to_csv(os.path.join(OUTPUT_DATASET, "statistic.csv"), index=False)

df = split_files(INPUT_IMAGE, OUTPUT_DATASET)
write_yaml(OUTPUT_DATASET)
save_df(OUTPUT_DATASET, df)
# %%
