import logging

# creating custom logger:
stream_logger = logging.getLogger(__name__)

# creating handlers for the custom logger:
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file-handler.log", 'a')

# setting severity level to the handlers:
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# setting the formatter for the custom logger:
stream_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y - %H:%M:%S")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y - %H:%M:%S")

# adding these formatter to the custom handler:
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

# adding these custom handlers to the custom logger:
stream_logger.addHandler(stream_handler)
stream_logger.addHandler(file_handler)

stream_logger.debug("This is debug message")
stream_logger.error("This is error message")