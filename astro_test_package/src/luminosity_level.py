import cv2
import pandas as pd
import openpyxl


def crop_image(activ, event):
    difer_in_width = int(abs(activ.shape[0] - event.shape[0])/2)
    difer_in_hight = int(abs(activ.shape[1] - event.shape[1])/2)
    if activ.size > event.size:
        cropped = activ[difer_in_width: - difer_in_width, difer_in_hight: - difer_in_hight]
    else:
        cropped = event[difer_in_width: - difer_in_width, difer_in_hight: - difer_in_hight]
    return cropped

def luminosity_level(event_df, activity_df):
    luminosity = []
    for i in event_df.index:
        if i < len(event_df.index) - 1:
            event = cv2.imread(event_df['image_path'][i],cv2.IMREAD_GRAYSCALE)
            activ = cv2.imread(activity_df['image_path'][i],cv2.IMREAD_GRAYSCALE)
            if activ.size > event.size:
                activ = crop_image(activ, event)
            x1, y1 = event.shape
            for x in range(0, x1):
                for y in range(0, y1):
                    if event[x, y] == 255:
                        luminosity.append(activ[x,y])
    level_of_lum = sum(luminosity)/len(luminosity)
    return level_of_lum

def save_data_luminosity_level(level_of_lum, name_table):
    data = []
    image_data = {
        'luminosity_level': level_of_lum}
    data.append(image_data)
    df = pd.DataFrame(data)
    print(df)
    df.to_excel(name_table)