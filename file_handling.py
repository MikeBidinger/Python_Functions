import tkinter as tk
from tkinter import filedialog
import os
import re
from datetime import datetime

def folder_selection_dialog(initial_dir:str='', title:str=''):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(
        initialdir=initial_dir, 
        title=title
    )
    return folder_path

def file_selection_dialog(file_types=[('All Files', '*.*')], initial_dir:str='', title:str=''):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=file_types, 
        initialdir=initial_dir, 
        title=title
    )
    return file_path

def get_latest_file(directory:str, file_name:str=''):
    creation_time = 0.0
    # Loop through directory
    for file in os.scandir(directory):
        # If object is a file
        if file.is_file():
            # If file expression matches
            if re.search(file_name, file.name):
                # Get creation datetime
                if os.path.getctime(file.path) > creation_time:
                    creation_time = os.path.getctime(file.path)
                    latestFile = file
                #print(datetime.utcfromtimestamp(creation_time), file.path)
    return latestFile

def get_latest_file_from_subfolder(directory:str, folder_name:str, file_name:str='', file_extention:str=''):
    creation_time = 0.0
    file_found = False
    # Loop through directory
    for subfolder in os.scandir(directory):
        if subfolder.is_dir() and folder_name in subfolder.name:
            for file in os.scandir(subfolder):
                # If object is a file
                if file.is_file():
                    # If file extension matches
                    if file_extention in file.name or file_extention == '':
                        # If filename matches
                        if re.search(file_name, file.name) or file_name == '':
                            # Get creation datetime
                            file_found = True
                            if os.path.getctime(file.path) > creation_time:
                                creation_time = os.path.getctime(file.path)
                                latest_file = file
                            #print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latest_file

def read_text(file_path:str):
    data = ''
    f = open(file_path, 'r')
    data = f.read()
    f.close()
    return data

def read_text_lines(file_path:str, nr_lines:int=0, encoding:str=None):
    data = []
    f = open(file_path, 'r', encoding=encoding)
    if nr_lines == 0:
        for x in f:
            data.append(x.replace('\n', ''))
    else:
        for i in range(0, nr_lines):
            data.append(f.readline())
    f.close()
    return data

def read_csv_data(file_path:str, key_headers:list, key_join:str, seperator:str=';', double_quotes:bool=False, encoding:str=None):
    data = {}
    f = open(file_path, 'r', encoding=encoding)
    data_str = f.read()
    f.close()
    data_str = data_str.replace('\n\n', ' ')
    while ';;' in data_str:
        data_str = data_str.replace(';;', ';"";')
    data_list = data_str.split('\n')
    data_str = ''
    start = True
    end = False
    for row in data_list:
        if start == False:
            if row != '':
                vals = row[1:len(row) - 1].split('"' + seperator + '"')
                keys = []
                for y in key_headers:
                    keys.append(vals[headers[y]])
                if key_join.join(keys) not in data:
                    data[key_join.join(keys)] = {}
                for idx, x in enumerate(vals):
                    data[key_join.join(keys)][header_list[idx]] = x
            else:
                if end == False:
                    end = True
                else:
                    print('Empty!')
        else:
            headers = {}
            header_list = row.split(seperator)
            for idy, y in enumerate(header_list):
                headers[y] = idy
            start = False
    return data

def write_result_list(results:list, folder_path:str, file_name:str, time_stamp:str, file_extension:str='.csv'):
    file_path = folder_path + file_name + "_" + time_stamp + file_extension
    #file_path = folder_path + file_name + ("_" + get_time_stamp() if time_stamp else "") + file_extension
    f = open(file_path, 'a')
    for result in results:
        f.write(result + '\n')
    f.close()
    return file_path

def get_time_stamp(date_only:bool=False):
    time_stamp = str(datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '_')
    if date_only:
        time_stamp = time_stamp.split('_')[0]
    return time_stamp
