import logging  # https://docs.python.org/3/library/logging.html

# Include and align timestamp, log-level, filename, function-name and the given message within the log-format
LOG_FORMAT = (
    "%(asctime)s - %(levelname)-8s - %(filename)s - %(funcName)s() - %(message)s"
)

# Set up teh logger
logging.basicConfig(
    level=logging.DEBUG,  # The level chosen determines what will be logged
    filename="log.log",  # Can be omitted to write logs only to the terminal
    filemode="w",  # Use the filemode "w" to create and overwrite and "a" to append
    format=LOG_FORMAT,  # Apply a specified log-format
)


def main():
    logging.debug("This a debug log.")
    logging.info("This a info log.")
    logging.warning("This a warning log.")
    logging.error("This a error log.")
    logging.critical("This a critical log.")


if __name__ == "__main__":
    main()
