import logging

def get_logger():
    logger = logging.getLogger("console_logger")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%d-%m-%Y %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger