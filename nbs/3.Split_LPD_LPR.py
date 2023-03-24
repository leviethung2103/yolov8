from PIL import Image
import os
import pandas as pd 

# Define the root directory where you want to start the search
root_dir = '/media/hunglv/T7/giangthanh_cambodia_new'

# Define a list of valid image extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']

data = []

# Use os.walk to recursively search through the root directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # Check if the file has a valid image extension
        # If it does, print the full path to the file
        full_path = os.path.join(dirpath, filename)
        image = Image.open(full_path)
        # Get the width and height of the image
        width, height = image.size
        
        if width == 1920:
            data += [dict(filename=full_path, width=width, height=height, full_size = True)]
        else:
            data += [dict(filename=full_path, width=width, height=height, full_size = False)]

df =  pd.DataFrame(data)
df.to_csv("giangthanh.csv",index=False)