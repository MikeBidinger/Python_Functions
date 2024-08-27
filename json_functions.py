import json


def main():
    # Functions in this module:
    read_json()
    write_json()


def read_json(file_path: str, mode: str = "r"):
    """Read the data from a JSON file.

    :param file_path: A string representing the source file path.
    :param mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    :return The data from the JSON file.
    """
    # Open the file from the given path in the specified mode
    with open(file_path, mode) as f:
        data = json.load(f)
    return data


def write_json(data, file_path: str, mode: str = "w"):
    """Write the data into a JSON file.
    
    :param data: Any valid JSON data.
    :param file_path: A string representing the destination file path.
    :param mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    :return A string representing the destination file path.
    """
    # Open the file from the given path in the specified mode
    with open(file_path, mode) as f:
        json.dump(data, f, indent=4)
    return file_path
