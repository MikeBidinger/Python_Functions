def main():
    # Functions in this module:
    string_to_list()
    string_to_matrix()
    matrix_to_string()
    matrix_to_dicts()
    dicts_to_matrix()
    string_to_dicts()
    dicts_to_string()


def string_to_list(string: str, separator: str = "\n", limit: int = 0) -> list[str]:
    """Parse a string into a list.
    - Args:
        - string: A string to parse.
        - separator: An optional string representing the separator within the given string.
        - limit: An optional integer representing the maximum number of returned list items.
    - Returns:
        - A list of strings.
    """
    # Parse string into list
    list = string.split(separator)
    # If limit is set
    if limit != 0:
        return list[:limit]
    return list


def string_to_matrix(
    string: str,
    row_sep: str = "\n",
    col_sep: str = ";",
    row_limit: int = 0,
    col_limit: int = 0,
) -> list[list[str]]:
    """Parse a string into a matrix. A matrix is a list of lists (2D-array).
    - Args:
        - string: A string to parse.
        - row_sep: An optional string representing the row-separator within the given string.
        - col_sep: An optional string representing the column-separator within the given string.
        - row_limit: An optional integer representing the maximum number of returned row items.
        - col_limit: An optional integer representing the maximum number of returned column items.
    - Returns:
        - A matrix data structure, a list of list (2D-array).
    """
    matrix = []
    # Parse string into list
    list = string_to_list(string, row_sep, row_limit)
    # Parse list into matrix
    for row in list:
        matrix.append(string_to_list(row, col_sep, col_limit))
    return matrix


def matrix_to_string(
    matrix: list[list], row_sep: str = "\n", col_sep: str = ";"
) -> str:
    """Parse a string into a matrix. A matrix is a list of lists (2D-array).
    - Args:
        - matrix: A matrix data structure, a list of list (2D-array).
        - row_sep: An optional string representing the row-separator that will be used for the returned string.
        - col_sep: An optional string representing the column-separator that will be used for the returned string.
    - Returns:
        - A string.
    """
    # Concatenate all values for each row
    string = col_sep.join(map(str, matrix[0]))
    for row in matrix[1:]:
        string += row_sep + col_sep.join(map(str, row))
    return string


def matrix_to_dicts(
    matrix: list[list], keys: list = [], filter_keys: list = []
) -> list[dict]:
    """Parse a matrix into a list of dictionaries. A matrix is a list of lists (2D-array).
    - Args:
        - matrix: A matrix data structure, a list of list (2D-array).
        - keys: An optional list representing the headers of the matrix if the matrix does not contain headers.
        - filter_keys: An optional list representing the headers of columns to be filtered.
    - Returns:
        - A list of dictionaries.
    """
    data = []
    # Get keys
    value_pos = 0
    if keys == []:
        keys = matrix[0]
        value_pos = 1
    # Get records
    for row in matrix[value_pos:]:
        record = {}
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


def dicts_to_matrix(data: list[dict], default: str = "") -> list[list]:
    """Parse a list of dictionaries into a matrix. A matrix is a list of lists (2D-array).
    - Args:
        - data: A list of dictionaries.
        - default: An optional string representing the value given to keys that do not exist.
    - Returns:
        - A matrix data structure, a list of list (2D-array).
    """
    matrix = []
    # Get keys
    keys = list(data[0].keys())
    matrix.append(keys)
    # Get values
    for record in data:
        row = []
        for key in keys:
            row.append(record.get(key, default))
        matrix.append(row)
    return matrix


def string_to_dicts(
    string: str,
    row_sep: str = "\n",
    col_sep: str = ";",
    row_limit: int = 0,
    keys: list = [],
    filter_keys: list = [],
) -> list[dict]:
    """Parse a string into a list of dictionaries.
    - Args:
        - string: A string to parse.
        - row_sep: An optional string representing the row-separator within the given string.
        - col_sep: An optional string representing the column-separator within the given string.
        - row_limit: An optional integer representing the maximum number of returned row items.
        - keys: An optional list representing the headers of the matrix if the matrix does not contain headers.
        - filter_keys: An optional list representing the headers of columns to be filtered.
    - Returns:
        - A list of dictionaries.
    """
    # Parse string into matrix
    matrix = string_to_matrix(string, row_sep, col_sep, row_limit)
    # Parse matrix into dictionaries
    return matrix_to_dicts(matrix, keys, filter_keys)


def dicts_to_string(
    data: list[dict], row_sep: str = "\n", col_sep: str = ";", default: str = ""
) -> str:
    """Parse a list of dictionaries into a string.
    - Args:
        - data: A list of dictionaries.
        - row_sep: An optional string representing the row-separator within the given string.
        - col_sep: An optional string representing the column-separator within the given string.
        - default: An optional string representing the value given to keys that do not exist.
    - Returns:
        - A string.
    """
    # Parse dictionaries into matrix
    matrix = dicts_to_matrix(data, default)
    # Parse matrix into string
    return matrix_to_string(matrix, row_sep, col_sep)
