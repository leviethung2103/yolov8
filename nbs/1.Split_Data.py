import os
import shutil

def split_files(directory):
    """
    This function takes a directory path and splits files with extensions .jpg and .png into an 'images' folder, 
    and files with extension .txt into a 'labels' folder.
    """
    images_dir = os.path.join(directory, 'images')
    labels_dir = os.path.join(directory, 'labels')

    # Create the 'images' and 'labels' folders if it doesn't exist
    try:
        os.mkdir(images_dir)
    except FileExistsError:
        pass
    try:
        os.mkdir(labels_dir)
    except FileExistsError:
        pass

    # Loop through all files in directory and move to appropriate folder based on extension
    for filename in os.listdir(directory):
        if not filename.startswith("."):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                shutil.move(os.path.join(directory, filename), images_dir)
            elif filename.endswith('.txt'):
                shutil.move(os.path.join(directory, filename), labels_dir)

directory_path = "/media/hunglv/T7/lpd_lao_chienkhuong_21022023_3000_v1.0/obj_train_data/ChienKhuong_21_02_2023_3k"
split_files(directory_path)


