import cv2
import matplotlib as plt
import openpyxl

def find_count_white_areas(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    white_areas_count = 0
    total_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        white_areas_count += 1
        total_area += area
    spatial_scale = 5.1
    if white_areas_count > 0:
        avg_area_in_mkm = total_area / (white_areas_count * (spatial_scale ** 2)) 
    else:
        avg_area_in_mkm = 0
    return white_areas_count, avg_area_in_mkm

def adding_information_about_white_areas(df):
    white_areas_count = []
    average_areas = []
    for image_path in df['image_path']:
        result_function_1 = find_count_white_areas(image_path)  
        white_areas_count.append(result_function_1[0])
        average_areas.append(result_function_1[1])
    df['white_areas_count'] = white_areas_count
    df['average_area'] = average_areas
    return df

def graph_average_area(df):
    df['time_seconds'] = df.index / 2
    time = df['time_seconds']
    average_area = df['average_area']
    gragh = plt.figure(figsize = (6.7, 3.11), dpi = 300)   
    plt.plot(time, average_area, color = 'limegreen', linewidth = 3)
    plt.xlabel('Время, c')
    plt.ylabel('Средняя площадь области, мкм²')
    plt.title('Средняя площадь области кальциевого события в зависимости от времени')
    plt.xlim(df['time_seconds'].min(), df['time_seconds'].max())
    plt.ylim(df['average_area'].min(), df['average_area'].max())
    plt.legend()
    plt.tight_layout()
    plt.show()
    return gragh

def save_graph(gragh, name_graph_png, name_graph_svg):
    gragh.savefig(name_graph_png)
    gragh.savefig(name_graph_svg)

def save_data_average_area(df, name_table):
    time_average_area_df = df[['time_seconds', 'average_area']].copy()
    print(time_average_area_df)
    time_average_area_df.to_excel(name_table)