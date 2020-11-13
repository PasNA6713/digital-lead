from loguru import logger


def get_file(file):
    logger.debug(file)
    # with open('example.jpg', 'wb') as f:
    #     f.write(file.read())