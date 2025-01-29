# Python Functions - [json_functions.py](json_functions.py)

Standardized JSON functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

## Content

-   [Functions](#functions):

    -   [read_json()](#read_json)
    -   [write_json()](#write_json)

# Functions

## read_json()

Read the data from a given JSON file path.

-   Args:

    -   `file_path` (`str`): A string representing the source file path.
    -   `mode` (`str`, optional): An string representing the mode in which the file is opened (e.g. `"w"` for write, `"a"` for append). Defaults to `"r"`.

-   Returns:

    -   `dict | list | str | int | bool | None`: The data from the JSON file.

```python
def read_json(file_path: str, mode: str = "r") -> dict | list | str | int | bool | None:
    with open(file_path, mode) as f:
        data: dict | list | str | int | bool | None = json.load(f)
    return data
```

## write_json()

Write the data into a JSON file.

-   Args:

    -   `data` (`dict | list | str | int | bool | None`): Any valid JSON data.
    -   `file_path` (`str`): A string representing the destination file path.
    -   `mode` (`str`, optional): An string representing the mode in which the file is opened (e.g. `"w"` for write, `"a"` for append). Defaults to `"w"`.

-   Returns:

    -   `str`: A string representing the destination file path.

```python
def write_json(
    data: dict | list | str | int | bool | None, file_path: str, mode: str = "w"
) -> str:
    with open(file_path, mode) as f:
        json.dump(data, f, indent=4)
    return file_path
```
