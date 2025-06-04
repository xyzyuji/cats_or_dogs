import logging

def get_logger():
    print("===================================================")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    print("===================================================")
    return logging.getLogger("cats_or_dogs_logger")
