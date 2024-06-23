import cv2
import numpy as np
import matplotlib as plt

def count_burning_times(df):
    image = cv2.imread(df['image_path'][0],cv2.IMREAD_GRAYSCALE)
    burning_times = np.zeros_like(image)
    for i in df.index:
        if i < len(df.index) - 1:
            image = cv2.imread(df['image_path'][i],cv2.IMREAD_GRAYSCALE)
            next_image = cv2.imread(df['image_path'][i+1],cv2.IMREAD_GRAYSCALE)
            if image.size == next_image.size:
                x1, y1 = image.shape
                for x in range(0, x1):
                    for y in range(0, y1):
                        if image[x, y] == 0 and next_image[x, y] == 255:
                            burning_times[x,y] += 1
    return burning_times

def getting_a_histogramm(burning_times):
    hist = plt.figure()   
    plt.pcolormesh(burning_times, cmap = 'inferno')
    plt.colorbar()
    plt.xlabel('Координаты пикселя по х')
    plt.ylabel('Координаты пикселя по у')
    plt.title('Светимость пикселей во времени')
    plt.show()
    return hist

def save_histogramm(hist, name_hist_png, name_hist_svg):
    hist.savefig(name_hist_png)
    hist.savefig(name_hist_svg)