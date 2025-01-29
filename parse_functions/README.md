# Python Functions - [parse_functions.py](parse_functions.py)

Standardized parse functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

## Content

-   [Functions](#functions):

    -   [string_to_list()](#string_to_list)
    -   [string_to_matrix()](#string_to_matrix)
    -   [matrix_to_string()](#matrix_to_string)
    -   [matrix_to_dicts()](#matrix_to_dicts)
    -   [dicts_to_matrix()](#dicts_to_matrix)
    -   [string_to_dicts()](#string_to_dicts)
    -   [dicts_to_string()](#dicts_to_string)

# Functions

## string_to_list()

Parse a string into a list.

-   Args:

    -   `string` (`str`): A string to parse.
    -   `separator` (`str`, optional): A string representing the separator within the given string. Defaults to `"\n"`.
    -   `limit` (`int`, optional): An integer representing the maximum number of returned list items. Defaults to `0`.

-   Returns:

    -   `list[str]`: A list of strings.

```python
def string_to_list(string: str, separator: str = "\n", limit: int = 0) -> list[str]:
    # Parse string into list
    list_str: list[str] = string.split(separator)
    # If limit is set
    if limit != 0:
        return list_str[:limit]
    return list_str
```

## string_to_matrix()

Parse a string into a matrix. A matrix is a list of lists (2D-array).

-   Args:

    -   `string` (`str`): A string to parse.
    -   `row_sep` (`str`, optional): A string representing the row-separator within the given string. Defaults to `"\n"`.
    -   `col_sep` (`str`, optional): A string representing the column-separator within the given string. Defaults to `";"`.
    -   `row_limit` (`int`, optional): An integer representing the maximum number of returned row items. Defaults to `0`.
    -   `col_limit` (`int`, optional): An integer representing the maximum number of returned column items. Defaults to `0`.

-   Returns:

    -   `list[list[str]]`: A matrix data structure, a list of list (2D-array).

```python
def string_to_matrix(
    string: str,
    row_sep: str = "\n",
    col_sep: str = ";",
    row_limit: int = 0,
    col_limit: int = 0,
) -> list[list[str]]:
    matrix: list = []
    # Parse string into list
    list_str: list[str] = string_to_list(string, row_sep, row_limit)
    # Parse list into matrix
    for row in list_str:
        matrix.append(string_to_list(row, col_sep, col_limit))
    return matrix
```

## matrix_to_string()

Parse a matrix into a string. A matrix is a list of lists (2D-array).

-   Args:

    -   `matrix` (`list[list]`): A matrix data structure, a list of list (2D-array).
    -   `row_sep` (`str`, optional): A string representing the row-separator that will be used for the returned string. Defaults to `"\n"`.
    -   `col_sep` (`str`, optional): A string representing the column-separator that will be used for the returned string. Defaults to `";"`.

-   Returns:

    -   `str`: A string parsed from the given matrix.

```python
def matrix_to_string(
    matrix: list[list], row_sep: str = "\n", col_sep: str = ";"
) -> str:
    # Concatenate all values for each row
    string: str = col_sep.join(map(str, matrix[0]))
    for row in matrix[1:]:
        string += row_sep + col_sep.join(map(str, row))
    return string
```

## matrix_to_dicts()

Parse a matrix into a list of dictionaries. A matrix is a list of lists (2D-array).

-   Args:

    -   `matrix` (`list[list]`): A matrix data structure, a list of list (2D-array).
    -   `keys` (`list`, optional): A list representing the headers of the matrix if the matrix does not contain headers. Defaults to `[]`.
    -   `filter_keys` (`list`, optional): A list representing the headers of columns to be filtered. Defaults to `[]`.

-   Returns:

    -   `list[dict]`: A list of dictionaries parsed from the given matrix.

```python
def matrix_to_dicts(
    matrix: list[list], keys: list = [], filter_keys: list = []
) -> list[dict]:
    data: list = []
    # Get keys
    value_pos: int = 0
    if keys == []:
        keys = matrix[0]
        value_pos = 1
    # Get records
    for row in matrix[value_pos:]:
        record: dict = {}
        # Get values
        for idy, key in enumerate(keys):
            record[key] = row[idy]
        # Add record
        data.append(record)
        if filter_keys != []:
            # Filter record by given keys
            data.append({key: record[key] for key in filter_keys})
        else:
            data.append(record)
    return data
```

## dicts_to_matrix()

Parse a list of dictionaries into a matrix. A matrix is a list of lists (2D-array).

-   Args:

    -   `data` (`list[dict]`): A list of dictionaries.
    -   `default` (`str`, optional): A string representing the value given to keys that do not exist. Defaults to `""`.

-   Returns:

    -   `list[list]`: A matrix data structure, a list of list (2D-array).

```python
def dicts_to_matrix(data: list[dict], default: str = "") -> list[list]:
    matrix: list = []
    # Get keys
    keys = list(data[0].keys())
    matrix.append(keys)
    # Get values
    for record in data:
        row: list = []
        for key in keys:
            row.append(record.get(key, default))
        matrix.append(row)
    return matrix
```

## string_to_dicts()

Parse a string into a list of dictionaries.

-   Args:

    -   `string` (`str`): A string to parse.
    -   `row_sep` (`str`, optional): A string representing the row-separator within the given string. Defaults to `"\n"`.
    -   `col_sep` (`str`, optional): A string representing the column-separator within the given string. Defaults to `";"`.
    -   `row_limit` (`int`, optional): An integer representing the maximum number of returned row items. Defaults to `0`.
    -   `keys` (`list`, optional): A list representing the headers of the matrix if the matrix does not contain headers. Defaults to `[]`.
    -   `filter_keys` (`list`, optional): A list representing the headers of columns to be filtered. Defaults to `[]`.

-   Returns:

    -   `list[dict]`: A list of dictionaries from the given string.

```python
def string_to_dicts(
    string: str,
    row_sep: str = "\n",
    col_sep: str = ";",
    row_limit: int = 0,
    keys: list = [],
    filter_keys: list = [],
) -> list[dict]:
    # Parse string into matrix
    matrix: list[list[str]] = string_to_matrix(string, row_sep, col_sep, row_limit)
    # Parse matrix into dictionaries
    return matrix_to_dicts(matrix, keys, filter_keys)
```

## dicts_to_string()

Parse a list of dictionaries into a string.

-   Args:

    -   `data` (`list[dict]`): A list of dictionaries.
    -   `row_sep` (`str`, optional): An optional string representing the row-separator within the given string. Defaults to `"\n"`.
    -   `col_sep` (`str`, optional): An optional string representing the column-separator within the given string. Defaults to `";"`.
    -   `default` (`str`, optional): An optional string representing the value given to keys that do not exist. Defaults to `""`.

-   Returns:

    -   `str`: A string parsed from the given list of dictionaries.

```python
def dicts_to_string(
    data: list[dict], row_sep: str = "\n", col_sep: str = ";", default: str = ""
) -> str:
    # Parse dictionaries into matrix
    matrix: list[list] = dicts_to_matrix(data, default)
    # Parse matrix into string
    return matrix_to_string(matrix, row_sep, col_sep)
```
