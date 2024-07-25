# Python Functions

Standardized function to save up repetitive work and keep code clean within
Python scripting. These all have basic formats and uses, but they can be
customized relatively easily to achieve tailored functionalities.

## Content:

-   **[File Handling](file_handling.py)**

    <details>
      <summary>Mostly file related functions. <h6>(Click to view/hide functions and descriptions.)</h6></summary><br>

    | Function                              | Description                                                                               |
    | ------------------------------------- | ----------------------------------------------------------------------------------------- |
    | _location_check()_                    | Check if the given path exists, if not keep looping with the given delay in seconds.      |
    | _directory_selection_dialog()_        | A directory selection dialog using the TKinter filedialog UI.                             |
    | _file_selection_dialog()_             | A file selection dialog using the TKinter filedialog UI.                                  |
    | _get_all_files()_                     | Return all file paths of a given directory (even for files within sub-directories).       |
    | _get_latest_file()_                   | Return the most recent (latest) created file in a given directory.                        |
    | _get_latest_file_from_subdirectory()_ | Return the most recent (latest) created file within a sub-directory of a given directory. |
    | _read_file()_                         | Read the data from a file.                                                                |
    | _read_xml()_[^1]                      | Read the data from a XML file and return it as an ordered dictionary.                     |
    | _read_file_lines()_                   | Read the data from a file, line by line.                                                  |
    | _write_file_list()_                   | Write a list of strings to a file.                                                        |
    | _get_time_stamp()_                    | Return the current timestamp.                                                             |
    | _prompt_message()_                    | Prompt the user with a message.                                                           |

    </details>

-   **[CSV Handling](csv_functions.py):**

    <details>
      <summary>Read and write CSV files. <h6>(Click to view/hide functions and descriptions.)</h6></summary><br>

    | Function              | Description                                                                   |
    | --------------------- | ----------------------------------------------------------------------------- |
    | _read_csv()_          | Read the data from a CSV file into a matrix[^2].                              |
    | _write_csv()_         | Write a matrix[^2] into a CSV file.                                           |
    | _create_csv()_        | Create a CSV file with the given field names.                                 |
    | _append_csv_record()_ | Append a dictionary record to the given CSV file.                             |
    | _read_csv_records()_  | Read the records from a CSV file into a list of dictionaries.                 |
    | _example_function()_  | Example of use: Create, append and read random example records to a CSV file. |

    </details>

-   **[JSON Handling](json_functions.py)**

    <details>
      <summary>Read and write JSON files. <h6>(Click to view/hide functions and descriptions.)</h6></summary><br>

    | Function       | Description                      |
    | -------------- | -------------------------------- |
    | _read_json()_  | Read the data from a JSON file.  |
    | _write_json()_ | Write the data into a JSON file. |

    </details>

-   **[Data Parsing](parse_functions.py)**

    <details>
      <summary>Parsing functions for multiple different data types and structures. <h6>(Click to view/hide functions and descriptions.)</h6></summary><br>

    | Function             | Description                                     |
    | -------------------- | ----------------------------------------------- |
    | _string_to_list()_   | Parse a string into a list.                     |
    | _string_to_matrix()_ | Parse a string into a matrix[^2].               |
    | _matrix_to_string()_ | Parse a matrix[^2] into a string.               |
    | _matrix_to_dicts()_  | Parse a matrix[^2] into a list of dictionaries. |
    | _dicts_to_matrix()_  | Parse a list of dictionaries into a matrix[^2]. |
    | _string_to_dicts()_  | Parse a string into a list of dictionaries.     |
    | _dicts_to_string()_  | Parse a list of dictionaries into a string.     |

    </details>

-   **[Logging](log_example.py)**

    How to log properly and well formatted using a configured logger (built-in Python module "[logging](https://docs.python.org/3/library/logging.html)").

-   **[Mail (Outlook) Functions](outlook.py)**

-   **[Keyboard Functions](Keyboard)**

-   **[Mouse Functions](Mouse)**

    <details>
      <summary>Automate mouse actions. <h6>(Click to view/hide functions and descriptions.)</h6></summary><br>

    | Function               | Description                                                           |
    | ---------------------- | --------------------------------------------------------------------- |
    | _get_mouse_position()_ | Get the current mouse position coordinates.                           |
    | _set_mouse()_          | Set the mouse position to a given position.                           |
    | _move_mouse()_         | Move the mouse position relative to the current mouse position.       |
    | _afk_movement()_       | Move the mouse position from a starting point for the given duration. |

    </details>

-   **[Application Functions](Application)**

[^1]: The function _read_xml()_ uses the module "[xmltodict](https://pypi.org/project/xmltodict/)". This module is not build-in with Python.
[^2]: A matrix is a list of lists (2D-array).
