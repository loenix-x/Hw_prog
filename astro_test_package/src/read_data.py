import os
import pandas as pd
from natsort import natsorted
import cv2

def create_folders_lists(main_path):
    event_folders = []
    activity_folders = []
    folder_names = []
    for folder_name in os.listdir(main_path):
        folder_names.append(folder_name)
        folder_path = os.path.join(main_path, folder_name)
        subfolders = os.listdir(folder_path)
        event_folder_path = os.path.join(folder_path, subfolders[0])
        activity_folder_path = os.path.join(folder_path, subfolders[1])

        event_folders.append(event_folder_path)
        activity_folders.append(activity_folder_path)

    return event_folders, activity_folders, folder_names

def create_dataframe(folder, name_dataset):
    data = []
    image_names = natsorted(os.listdir(folder))  
    for image_name in image_names:
        image_path = os.path.join(folder, image_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_data = {
            'dataset': name_dataset,
            'image_name': image_name,
            'image_path': image_path,
            'image_size': image.shape}
        data.append(image_data)
    df = pd.DataFrame(data)
    return df