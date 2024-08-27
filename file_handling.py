import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
from datetime import datetime
import time
import xmltodict  # https://pypi.org/project/xmltodict/ - This module is not build-in with Python
from collections import OrderedDict


def main():
    # Functions in this module:
    location_check()
    directory_selection_dialog()
    file_selection_dialog()
    get_all_files()
    get_latest_file()
    get_latest_file_from_subdirectory()
    read_file()
    read_xml()
    read_file_lines()
    write_file_list()
    get_time_stamp()
    prompt_message()


def location_check(path: str, retries: int = 12, delay: int = 5) -> bool:
    """Check if the given path exists, if not keep looping with the given delay in seconds.

    :param path: A string representing the path (e.g. file or directory).
    :param retries: An optional integer representing the number of retries (default = 12 retries).
    :param delay: An optional integer representing the retry-delay in seconds (default = 5 sec).
    :return: A boolean, True when the path is found, False if the path is not found after the given retries.
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


def directory_selection_dialog(initial_dir: str = "", title: str = "") -> str:
    """A directory selection dialog using the TKinter filedialog UI.

    :param initial_dir: A string specifying the initial directory.
    :param title: A string specifying the title of the dialog.
    :return: A string containing the path of the selected directory.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    directory_path = filedialog.askdirectory(
        initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return directory_path


def file_selection_dialog(
    file_types=[("All Files", "*.*")], initial_dir: str = "", title: str = ""
) -> str:
    """A file selection dialog using the TKinter filedialog UI.

    :param file_types: A list with tuples of predefined file types (e.g. [("CSV Files", "*.csv")]).
    :param initial_dir: A string specifying the initial directory.
    :param title: A string specifying the title of the dialog.
    :return: A string containing the path of the selected file.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=file_types, initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return file_path


def get_all_files(directory: str, search_pattern: str = "") -> list[str]:
    """Return all file paths of a given directory (even for files within sub-directories).

    :param directory: A string specifying the directory.
    :param search_pattern: An optional string specifying the pattern which need to comply with the files.
    :return: A list of strings containing all file paths.
    """
    file_paths = []
    for _, _, files in os.walk(directory):
        for f in files:
            if search_pattern in f:
                path = os.path.join(directory, f)
                file_paths.append(path)
    return file_paths


def get_latest_file(directory: str, file_pattern: str = "") -> str | None:
    """Return the most recent (latest) created file in a given directory.

    :param directory: A string specifying the directory.
    :param file_pattern: An optional string specifying the pattern which need to comply with the filename.
    :return: A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
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
                    latestFile = file.path
                # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latestFile


def get_latest_file_from_subdirectory(
    directory: str, directory_name: str, file_pattern: str = ""
) -> str | None:
    """Return the most recent (latest) created file within a sub-directory of a given directory.

    :param directory: A string specifying the directory.
    :param directory_name: A string specifying the name of the sub-directory (partial name is possible as well).
    :param file_pattern: An optional string specifying the pattern which need to comply with the filename.
    :return: A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
    """
    creation_time = 0.0
    file_found = False
    # Loop through directory
    for subdir in os.scandir(directory):
        if subdir.is_dir() and directory_name in subdir.name:
            for file in os.scandir(subdir):
                # If object is a file
                if file.is_file():
                    # If filename matches
                    if re.search(file_pattern, file.name):
                        # Get creation datetime
                        file_found = True
                        if os.path.getctime(file.path) > creation_time:
                            creation_time = os.path.getctime(file.path)
                            latest_file = file.path
                        # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latest_file


def read_file(file_path: str, encoding: str = None) -> str:
    """Read the data from a file.

    :param file_path: A string representing the file path.
    :param encoding: An optional string representing the encoding.
    :return: A string containing the data of the given file.
    """
    data = ""
    with open(file_path, "r", encoding=encoding) as f:
        data = f.read()
    return data


def read_xml(file_path: str) -> OrderedDict:
    """Read the data from a XML file and return it as an ordered dictionary.

    :param file_path: A string representing the file path.
    :return: An ordered dictionary containing the data of the XML file.
    """
    data = ""
    with open(file_path, "r") as f:
        data = xmltodict.parse(f.read())
    return data


def read_file_lines(
    file_path: str, nr_lines: int = -1, encoding: str = None
) -> list[str]:
    """Read the data from a file, line by line.

    :param file_path: A string representing the file path.
    :param nr_lines: An optional integer representing the number of lines to read.
    :param encoding: An optional string representing the encoding.
    :return: A list of strings containing the data of the file.
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


def write_file_list(results: list[str], file_path: str, mode: str = "w") -> str:
    """Write a list of strings to a file.

    **CAUTION**: By default if the file path already exists, it will be overwritten.

    :param results: A list of strings to write to the file.
    :param file_path: A string representing the path of the destination file.
    :param mode: An optional string representing the mode (e.g. "w" for write, "a" for append).
    :return: A string containing the path of the destination file.
    """
    with open(file_path, mode) as f:
        for result in results:
            f.write(result)
            f.write("\n")
    return file_path


def get_time_stamp(date_only: bool = False) -> str:
    """Return the current timestamp.

    :param date_only: An optional boolean, True if only the date (excluding time) has to be returned.
    :return: A string containing the current timestamp (including or excluding time, depending on the given optional argument).
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
    - Types of massage boxes (value of parameter **type**):
        | Value       | Description                                                                                  |
        | ----------- | -------------------------------------------------------------------------------------------- |
        | info        | Displays an information message box                                                          |
        | warning     | Displays a warning message box                                                               |
        | error       | Displays an error message box                                                                |
        | question    | Ask a question, returns the symbolic name of the selected button                             |
        | okcancel    | Ask if operation should proceed, returns True if the answer is "ok" and False otherwise      |
        | retrycancel | Ask if operation should be retried, return True if the answer is "retry" and False otherwise |
        | yesno       | Ask a question, returns True if the answer is "yes" and False if "no"                        |
        | yesnocancel | Ask a question, returns True if the answer is "yes", False if "no", and None otherwise       |

    :param type: The type of the message box
    :param title: A string representing the title of the prompt.
    :param message: A string representing the message of the prompt.
    :return: A boolean or string (depending on the type argument) containing the users answer of the asked question.
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
