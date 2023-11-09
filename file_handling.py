import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
from datetime import datetime
import time
import xmltodict


def location_check(path: str, retries: int = 12, delay: int = 5):
    """Check if the file or folder location exists, if not keep looping with the given delay in seconds.
    - Args:
        - path: A string representing the file or folder location.
        - retries: An optional integer representing the number of retries (default = 12 retries).
        - delay: An optional integer representing the delay in seconds (default = 5 sec).
    - Returns:
        - True when the network connection exists.
    """
    if not os.path.exists(path):
        msg_str = f"'{path}' doesn't exists! Retrying in {delay} seconds."
        for i in range(retries + 1):
            if i != 0:
                print(f"ERROR {datetime.now()}:", msg_str, f"Retry {i}/{retries}")
            else:
                print(f"ERROR {datetime.now()}:", msg_str)
            time.sleep(delay)
            if os.path.exists(path):
                print(f"'{path}' exists!\n")
                break
        else:
            return False
    return True


def folder_selection_dialog(initial_dir: str = "", title: str = ""):
    """A folder selection dialog using the TKinter filedialog UI.
    - Args:
        - initial_dir: A string specifying the initial directory.
        - title: A string specifying the title of the dialog.
    - Returns:
        - The path of the selected folder.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    folder_path = filedialog.askdirectory(
        initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return folder_path


def file_selection_dialog(
    file_types=[("All Files", "*.*")], initial_dir: str = "", title: str = ""
):
    """A file selection dialog using the TKinter filedialog UI.
    - Args:
        - file_types: A list with tuples of predefined file types.
        - initial_dir: A string specifying the initial directory.
        - title: A string specifying the title of the dialog.
    - Returns:
        - The path of the selected file.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=file_types, initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return file_path


def get_all_files(directory: str, search_pattern: str = ""):
    """Get all file paths of a given directory (even for files within sub-directories).
    - Args:
        - directory: A string specifying the directory.
        - search_pattern: An optional string specifying the pattern which need to comply with the files.
    - Returns:
        - A list of strings containing all file paths.
    """
    file_paths = []
    for _, _, files in os.walk(directory):
        for f in files:
            if search_pattern in f:
                path = os.path.join(directory, f)
                file_paths.append(path)
    return file_paths


def get_latest_file(directory: str, file_pattern: str = ""):
    """Get the most recent (latest) created file in a given directory.
    - Args:
        - directory: A string specifying the directory.
        - file_pattern: An optional string specifying the pattern which need to comply with the filename.
    - Returns:
        - A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
    """
    creation_time = 0.0
    file_found = False
    # Loop through directory
    for file in os.scandir(directory):
        # If object is a file
        if file.is_file():
            # If file expression matches
            if re.search(file_pattern, file.name):
                # Get creation datetime
                file_found = True
                if os.path.getctime(file.path) > creation_time:
                    creation_time = os.path.getctime(file.path)
                    latestFile = file
                # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latestFile


def get_latest_file_from_subfolder(
    directory: str, directory_name: str, file_name: str = "", file_extension: str = ""
):
    """Get the most recent (latest) created file within a sub-directory of a given directory.
    - Args:
        - directory: A string specifying the directory.
        - directory_name: A string specifying the name of the sub-directory (partial name is possible as well).
    - Returns:
        - A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
    """
    creation_time = 0.0
    file_found = False
    # Loop through directory
    for subfolder in os.scandir(directory):
        if subfolder.is_dir() and directory_name in subfolder.name:
            for file in os.scandir(subfolder):
                # If object is a file
                if file.is_file():
                    # If file extension matches
                    if file_extension in file.name or file_extension == "":
                        # If filename matches
                        if re.search(file_name, file.name) or file_name == "":
                            # Get creation datetime
                            file_found = True
                            if os.path.getctime(file.path) > creation_time:
                                creation_time = os.path.getctime(file.path)
                                latest_file = file
                            # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latest_file


def read_text(file_path: str, encoding: str = None):
    """Read the data from a text file.
    - Args:
        - file_path: A string representing the filepath.
        - encoding: A string representing the encoding.
    - Returns:
        - A string containing the data of the CSV file.
    """
    data = ""
    with open(file_path, "r", encoding=encoding) as f:
        data = f.read()
    return data


def read_xml(file_path: str):
    """Read the data from a XML file and return it as an ordered dictionary.
    - Args:
        - file_path: A string representing the filepath.
    - Returns:
        - An ordered dictionary containing the data of the XML file.
    """
    data = ""
    with open(file_path, "r") as f:
        data = xmltodict.parse(f.read())
    return data


def read_text_lines(file_path: str, nr_lines: int = -1, encoding: str = None):
    """Read the data from a text file, line by line.
    - Args:
        - file_path: A string representing the filepath.
        - nr_lines: An integer representing the number of lines to read.
        - encoding: A string representing the encoding.
    - Returns:
        - A list of strings containing the data of the CSV file.
    """
    data = []
    with open(file_path, "r", encoding=encoding) as f:
        if nr_lines < 1:
            for x in f:
                data.append(x.replace("\n", ""))
        else:
            for _ in range(0, nr_lines):
                data.append(f.readline())
    return data


def read_csv_data(
    file_path: str,
    separator: str = ";",
    double_quotes: bool = False,
    encoding: str = None,
):
    """Read the data from a CSV file.
    - Args:
        - file_path: A string representing the filepath.
        - separator: A string representing the separator of the CSV file.
        - double_quotes: A boolean representing whether to dispose the double quotes within the CSV file.
        - encoding: A string representing the encoding.
    - Returns:
        - A list of dictionaries containing the data of the CSV file in header and value pairs.
    """
    data = []
    rows = read_text_lines(file_path, encoding=encoding)
    if double_quotes:
        headers = rows[0][1:-1].split(f'"{separator}"')
    else:
        headers = rows[0].split(separator)
    for row in rows[1:]:
        data_row = {}
        if double_quotes:
            values = row[1:-1].split(f'"{separator}"')
        else:
            values = row.split(separator)
        for i in range(len(values)):
            data_row[headers[i]] = values[i]
        data.append(data_row)
    return data


def write_result_list(
    results: list,
    directory_path: str,
    file_name: str,
    time_stamp: str,
    file_extension: str = ".csv",
):
    """Write a list of data to a file.
    - Args:
        - results: A list of data to write.
        - directory_path: A string representing the directory path of the destination file.
        - file_name: A string representing the name of the destination file.
        - time_stamp: A string representing the current time of the creation of the destination file.
        - file_extension: An optional string representing the extension of the destination file.
    - Returns:
        - A string containing the entire file's destination path.
    """
    file_path = directory_path + file_name + "_" + time_stamp + file_extension
    # file_path = directory_path + file_name + ("_" + get_time_stamp() if time_stamp else "") + file_extension
    with open(file_path, "a") as f:
        for result in results:
            f.write(result + "\n")
    return file_path


def get_time_stamp(date_only: bool = False):
    """Get the current timestamp.
    - Args:
        - date_only: An optional boolean, True if only the date (excluding time) has to be returned.
    - Returns:
        - A string containing the current timestamp (including or excluding time, depending on the given optional argument).
    """
    time_stamp = (
        str(datetime.now())
        .replace("-", "")
        .replace(":", "")
        .replace(".", "")
        .replace(" ", "_")
    )
    if date_only:
        return time_stamp.split("_")[0]
    return time_stamp


def prompt_message(type, title, message):
    """Prompt the user with a message.
    - Args:
        - type:
            - info: Displays an information message box
            - warning: Displays a warning message box
            - error: Displays a error message box
            - question: Ask a question, returns the symbolic name of the selected button.
            - okcancel: Ask if operation should proceed, returns True if the answer is "ok" and False otherwise.
            - retrycancel: Ask if operation should be retried, return True if the answer is "retry" and False otherwise.
            - yesno: Ask a question, returns True if the answer is "yes" and False if "no".
            - yesnocancel: Ask a question, returns True if the answer is "yes", False if "no", and None otherwise.
        - title: A string representing the title of the prompt.
        - message: A string representing the message of the prompt.
    - Returns:
        - A boolean or string (depending on the type argument) containing the users answer of the asked question.
    """
    result = None
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    if type == "info":
        messagebox.showinfo(title, message, parent=root)
    elif type == "warning":
        messagebox.showwarning(title, message, parent=root)
    elif type == "error":
        messagebox.showerror(title, message, parent=root)
    elif type == "question":
        result = messagebox.askquestion(title, message, parent=root)
    elif type == "okcancel":
        result = messagebox.askokcancel(title, message, parent=root)
    elif type == "retrycancel":
        result = messagebox.askretrycancel(title, message, parent=root)
    elif type == "yesno":
        result = messagebox.askyesno(title, message, parent=root)
    elif type == "yesnocancel":
        result = messagebox.askyesnocancel(title, message, parent=root)
    root.destroy()
    return result
