import csv  # https://docs.python.org/3/library/csv.html
from random import randint
from pprint import pprint as pp


def main():
    # Functions in this module:
    read_csv()
    write_csv()
    create_csv()
    append_csv_record()
    read_csv_records()
    example_function()


def read_csv(
    file_path: str, delimiter: str = ";", mode: str = "r", encoding=None
) -> list[list]:
    """Read the data from a CSV file into a matrix. A matrix is a list of lists (2D-array).
    
    :param file_path: A string representing the source file path.
    :param delimiter: An optional string representing the delimiter of the CSV file.
    :param mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    :param encoding: An optional string representing the encoding of the file.
    :return: A matrix data structure, a list of list (2D-array).
    """
    matrix = []
    # Open the file from the given path in the specified mode
    with open(file_path, mode, encoding=encoding) as f:
        # Create a CSV reader
        reader = csv.reader(f, delimiter=delimiter)
        # Read each row from the CSV file and append it to the matrix
        for row in reader:
            matrix.append(row)
    return matrix


def write_csv(
    matrix: list[list], file_path: str, delimiter: str = ";", mode: str = "w"
) -> str:
    """Write a matrix into a CSV file. A matrix is a list of lists (2D-array).
    
    :param matrix: A matrix data structure, a list of list (2D-array).
    :param file_path: A string representing the destination file path.
    :param delimiter: An optional string representing the delimiter of the CSV file.
    :param mode: An optional string representing the mode in which the file is opened (e.g. "w" for write, "a" for append).
    :return: A string representing the destination file path.
    """
    # Open the file from the given path in the specified mode
    with open(file_path, mode) as f:
        # Create a CSV writer
        writer = csv.writer(f, delimiter=delimiter)
        # Write each row from the matrix to the CSV file
        for row in matrix:
            writer.writerow(row)
    return file_path


def create_csv(file_path: str, field_names: list[str], delimiter: str = ";") -> str:
    """Create a CSV file with the given field names.
    
    :param file_path: A string representing the destination file path.
    :param field_names: A list of strings representing the field names.
    :param delimiter: An optional string representing the delimiter of the CSV file.
    :return: A string representing the destination file path.
    """
    # Open the file from the given path in the write mode
    with open(file_path, "w") as f:
        # Create a CSV writer
        writer = csv.writer(f, delimiter=delimiter)
        # Write the field names to the CSV file
        writer.writerow(field_names)
    return file_path


def append_csv_record(
    file_path: str, field_names: list[str], record: dict, delimiter: str = ";"
) -> str:
    """Append a dictionary record to the given CSV file.
    
    :param file_path: A string representing the destination file path.
    :param field_names: A list of strings representing the field names.
    :param record: A dictionary representing the record to be written.
    :param delimiter: An optional string representing the delimiter of the CSV file.
    :return: A string representing the destination file path.
    """
    # Open the file from the given path in the append mode
    with open(file_path, "a") as f:
        # Create a CSV writer
        writer = csv.DictWriter(f, fieldnames=field_names, delimiter=delimiter)
        # Append the record to the CSV file
        writer.writerow(record)
    return file_path


def read_csv_records(
    file_path: str, field_names: list[str] = None, delimiter: str = ";"
) -> list[dict]:
    """Read the records from a CSV file into a list of dictionaries.
    
    :param file_path: A string representing the source file path.
    :param field_names: An optional list of strings representing the field names.
    :param delimiter: An optional string representing the delimiter of the CSV file.
    :return: A list of dictionaries representing the records from the CSV file.
    """
    records = []
    # Open the file from the given path in the read mode
    with open(file_path, "r") as f:
        # Create a CSV reader
        reader = csv.DictReader(f, fieldnames=field_names, delimiter=delimiter)
        # Read each record from the CSV file and append it to the records list
        for record in reader:
            records.append(record)
    return records


def example_function():
    """Example of use:
    Create, append and read random example records to a CSV file.
    """
    file_path = "example.csv"
    field_names = ["ID", "Field_A", "Field_B", "Field_C"]
    # Create random example records
    records = []
    for i in range(5):
        record = {"ID": i + 1}
        for x, field in enumerate(field_names[1:]):
            record[field] = randint((x + 1) * 10 + 1, (x + 1) * 10 + 9)
        records.append(record)
    # Create CSV file with field names
    create_csv(file_path, field_names)
    # Append records to CSV file
    for record in records:
        append_csv_record(file_path, field_names, record)
    # Read records from CSV file
    result = read_csv_records(file_path)
    pp(result)


if __name__ == "__main__":
    example_function()
