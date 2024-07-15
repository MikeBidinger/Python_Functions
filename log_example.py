import logging  # https://docs.python.org/3/library/logging.html

# Include and align timestamp, log-level, filename, function-name and the given message within the log-format
LOG_FORMAT = (
    "%(asctime)s - %(levelname)-8s - %(filename)s - %(funcName)s() - %(message)s"
)

# Set up logging to a file named "log.log" with debug level and write mode, and the log format defined above.
logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    filemode="w",
    format=LOG_FORMAT,
)


def main():
    log_a_debug("This a debug log.")
    log_a_info("This a info log.")
    log_a_warning("This a warning log.")
    log_a_error("This a error log.")
    log_a_critical("This a critical log.")


def log_a_debug(msg: object, stack_info: bool = False):
    logging.debug(msg, stack_info=stack_info)


def log_a_info(msg: object, stack_info: bool = False):
    logging.info(msg, stack_info=stack_info)


def log_a_warning(msg: object, stack_info: bool = False):
    logging.warning(msg, stack_info=stack_info)


def log_a_error(msg: object, stack_info: bool = False):
    logging.error(msg, stack_info=stack_info)


def log_a_critical(msg: object, stack_info: bool = False):
    logging.critical(msg, stack_info=stack_info)


if __name__ == "__main__":
    main()
