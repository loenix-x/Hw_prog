import read_data as rd
import average_area as aa
import os
import burning_times as bt
import luminosity_level as ll

def function_runs_all_functions(main_path):
    event_folders, activity_folders, folder_names  = rd.create_folders_lists(main_path)
    
    for i in range(len(event_folders)):
        event_path = event_folders[i]
        activity_path = activity_folders[i]
        events_df = rd.create_dataframe(event_path, 'event')
        activities_df = rd.create_dataframe(activity_path, 'activity')
        events_df = aa.adding_information_about_white_areas(events_df)
        graph_average = aa.graph_average_area(events_df)
        folder_name = folder_names[i]
        path_to_save = rf'C:\Hw_prog\astro-test-pacage\results\{folder_name}'
        os.chdir(path_to_save)
        aa.save_graph(graph_average, f'График средней площади_{i + 1}.png', f'График средней площади_{i + 1}.svg')
        aa.save_data_average_area(events_df, f'Таблица средней площади_{i + 1}.xlsx')

        burning_times = bt.count_burning_times(events_df)
        hist_of_burning_times = bt.getting_a_histogramm(burning_times)
        bt.save_histogramm(hist_of_burning_times, f'Колличества моментов времени, когда пиксель начинал гореть_{i + 1}.png', f'Колличества моментов времени, когда пиксель начинал гореть_{i + 1}.svg')
        
        level_of_lum = ll.luminosity_level(events_df, activities_df)
        ll.save_data_luminosity_level(level_of_lum, f'Таблица среднего уровня светимости_{i + 1}.xlsx')