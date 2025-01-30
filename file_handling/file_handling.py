import xmltodict  # https://pypi.org/project/xmltodict/ - This module is not build-in with Python

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
from datetime import datetime
import time
from collections import OrderedDict
from enum import Enum


def location_check(path: str, retries: int = 12, delay: int = 5) -> bool:
    """Check if the given path exists, if not keep looping with the given delay in seconds.

    Args:
        -   `path` (`str`): A string representing the path (e.g. file or directory).
        -   `retries` (`int`, optional): An integer representing the number of retries. Defaults to `12`.
        -   `delay` (`int`, optional): An integer representing the retry-delay in seconds. Defaults to `5`.

    Returns:
        -   `bool`: A boolean, True when the path is found, False if the path is not found after the given retries.
    """
    if not os.path.exists(path):
        msg_str: str = f"'{path}' doesn't exists! Retrying in {delay} seconds."
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

    Args:
        -   `initial_dir` (`str`, optional): A string specifying the initial directory. Defaults to `""`.
        -   `title` (`str`, optional): A string specifying the title of the dialog. Defaults to `""`.

    Returns:
        -   `str`: A string containing the path of the selected directory.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    directory_path: str = filedialog.askdirectory(
        initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return directory_path


def file_selection_dialog(
    file_types: list[tuple[str, str]] = [("All Files", "*.*")],
    initial_dir: str = "",
    title: str = "",
) -> str:
    """A file selection dialog using the TKinter filedialog UI.

    Args:
        -   `file_types` (`list`, optional): A list with tuples of predefined file types (e.g. `[("CSV Files", "*.csv")]`). Defaults to `[("All Files", "*.*")]`.
        -   `initial_dir` (`str`, optional): A string specifying the initial directory. Defaults to `""`.
        -   `title` (`str`, optional): A string specifying the title of the dialog. Defaults to `""`.

    Returns:
        -   `str`: A string containing the path of the selected file.
    """
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    file_path: str = filedialog.askopenfilename(
        filetypes=file_types, initialdir=initial_dir, title=title, parent=root
    )
    root.destroy()
    return file_path


def get_all_files(directory: str, search_pattern: str = "") -> list[str]:
    """Return all file paths of a given directory (even for files within sub-directories).

    Args:
        -   `directory` (`str`): A string specifying the directory.
        -   `search_pattern` (`str`, optional): A string specifying the pattern which need to comply with the files. Defaults to `""`.

    Returns:
        -   `list[str]`: A list of strings containing all file paths.
    """
    file_paths: list[str] = []
    for _, _, files in os.walk(directory):
        for f in files:
            if search_pattern in f:
                path: str = os.path.join(directory, f)
                file_paths.append(path)
    return file_paths


def get_latest_file(directory: str, file_pattern: str = "") -> str | None:
    """Return the most recent (latest) created file in a given directory.

    Args:
        -   `directory` (`str`): A string specifying the directory.
        -   `file_pattern` (`str`, optional): A string specifying the pattern which need to comply with the filename. Defaults to `""`.

    Returns:
        -   `str | None`: A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
    """
    latest_file: str | None = None
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
                    creation_time: float = os.path.getctime(file.path)
                    latest_file = file.path
                # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latest_file


def get_latest_file_from_subdirectory(
    directory: str, directory_name: str, file_pattern: str = ""
) -> str | None:
    """Return the most recent (latest) created file within a sub-directory of a given directory.

    Args:
        -   `directory` (`str`): A string specifying the directory.
        -   `directory_name` (`str`): A string specifying the name of the sub-directory (partial name is possible as well).
        -   `file_pattern` (`str`, optional): A string specifying the pattern which need to comply with the filename. Defaults to `""`.

    Returns:
        -   `str | None`: A strings containing the most recent (latest) created file path if the file is found, otherwise None will be returned.
    """
    latest_file: str | None = None
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
                            creation_time: float = os.path.getctime(file.path)
                            latest_file = file.path
                        # print(datetime.utcfromtimestamp(creation_time), file.path)
    if file_found:
        return latest_file


def read_file(file_path: str, encoding: str | None = None) -> str:
    """Read the data from a file.

    Args:
        -   `file_path` (`str`): A string representing the file path.
        -   `encoding` (`str | None`, optional): A string representing the encoding. Defaults to `None`.

    Returns:
        -   `str`: A string containing the data of the given file.
    """
    data: str = ""
    with open(file_path, "r", encoding=encoding) as f:
        data = f.read()
    return data


def read_xml(file_path: str) -> OrderedDict:
    """Read the data from a XML file and return it as an ordered dictionary.

    Args:
        -   `file_path` (`str`): A string representing the file path.

    Returns:
        -   `OrderedDict`: An ordered dictionary containing the data of the XML file.
    """
    data: OrderedDict = OrderedDict()
    with open(file_path, "r") as f:
        data = xmltodict.parse(f.read())
    return data


def read_file_lines(
    file_path: str, nr_lines: int = -1, encoding: str | None = None
) -> list[str]:
    """Read the data from a file, line by line.

    Args:
        -   `file_path` (`str`): A string representing the file path.
        -   `nr_lines` (`int`, optional): An integer representing the number of lines to read. Defaults to `-1`.
        -   `encoding` (`str | None`, optional): A string representing the encoding. Defaults to `None`.

    Returns:
        -   `list[str]`: A list of strings containing the data of the file.
    """
    data: list[str] = []
    with open(file_path, "r", encoding=encoding) as f:
        if nr_lines < 1:
            for line in f:
                data.append(line.replace("\n", ""))
        else:
            for _ in range(0, nr_lines):
                data.append(f.readline())
    return data


def write_file_list(results: list[str], file_path: str, mode: str = "w") -> str:
    """Write a list of strings to a file.

    CAUTION: By default the file will be overwritten, if the file path already exists.

    Args:
        -   `results` (`list[str]`): A list of strings to write to the file.
        -   `file_path` (`str`): A string representing the path of the destination file.
        -   `mode` (`str`, optional): A string representing the mode (e.g. `"w"` for write, `"a"` for append). Defaults to `"w"`.

    Returns:
        -   `str`: A string containing the path of the destination file.
    """
    with open(file_path, mode) as f:
        for result in results:
            f.write(result)
            f.write("\n")
    return file_path


def get_time_stamp(date_only: bool = False) -> str:
    """Return the current timestamp.

    Args:
        -   `date_only` (`bool`, optional): A boolean, `True` if only the date (excluding time) has to be returned. Defaults to `False`.

    Returns:
        -   `str`: A string containing the current timestamp (including or excluding time, depending on the given argument).
    """
    time_stamp: str = (
        str(datetime.now())
        .replace("-", "")
        .replace(":", "")
        .replace(".", "")
        .replace(" ", "_")
    )
    if date_only:
        return time_stamp.split("_")[0]
    return time_stamp


class MessageBoxType(Enum):
    """Types of massage boxes.

    `Enum` (`str`):

    | Value         | Description                                                                                        |
    | ------------- | -------------------------------------------------------------------------------------------------- |
    | `info`        | Displays an information message box                                                                |
    | `warning`     | Displays a warning message box                                                                     |
    | `error`       | Displays an error message box                                                                      |
    | `question`    | Ask a question, returns the symbolic name of the selected button                                   |
    | `okcancel`    | Ask if operation should proceed, returns `True` if the answer is `ok` and `False` otherwise        |
    | `retrycancel` | Ask if operation should be retried, return `True` if the answer is `retry` and `False` otherwise   |
    | `yesno`       | Ask a question, returns `True` if the answer is `yes` and `False` if `no`                          |
    | `yesnocancel` | Ask a question, returns `True` if the answer is `yes`, `False` if `no`, and `None` otherwise       |
    """

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    QUESTION = "question"
    OKCANCEL = "okcancel"
    RETRYCANCEL = "retrycancel"
    YESNO = "yesno"
    YESNOCANCEL = "yesnocancel"


def prompt_message(type: MessageBoxType, title: str, message: str) -> None | str | bool:
    """Prompt the user with a message.

    Args:
        -   `type` (`MessageBoxType`): The type of the message box.
        -   `title` (`str`): A string representing the title of the prompt.
        -   `message` (`str`): A string representing the message of the prompt.

    Returns:
        -   `None | str | bool`: A boolean or string (depending on the type argument) containing the users answer of the asked question.
    """
    result: str | bool | None = None
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
