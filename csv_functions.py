import csv


def main():
    # Functions in this module:
    read_csv()
    write_csv()


def read_csv(file_path: str, delimiter: str = ";", mode: str = "r") -> list[list]:
    """Read the data from a CSV file into a matrix. A matrix is a list of lists (2D-array).
    - Args:
        - file_path: A string representing the source file path.
        - delimiter: An optional string representing the delimiter of the CSV file.
        - mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    - Returns:
        - A matrix data structure, a list of list (2D-array).
    """
    matrix = []
    # Open the file from the given path in the specified mode
    with open(file_path, mode) as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        # Read each row from the CSV file and append it to the matrix
        for row in csv_reader:
            matrix.append(row)
    return matrix


def write_csv(
    matrix: list[list], file_path: str, delimiter: str = ";", mode: str = "w"
) -> str:
    """Write a matrix into a CSV file. A matrix is a list of lists (2D-array).
    - Args:
        - matrix: A matrix data structure, a list of list (2D-array).
        - file_path: A string representing the destination file path.
        - delimiter: An optional string representing the delimiter of the CSV file.
        - mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    - Returns:
        - A string representing the destination file path.
    """
    # Open the file from the given path in the specified mode
    with open(file_path, mode) as f:
        writer = csv.writer(f, delimiter=delimiter)
        # Write each row from the matrix to the CSV file
        for row in matrix:
            writer.writerow(row)
    return file_path
