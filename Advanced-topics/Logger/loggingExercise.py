import logging
from custom_logger import custom_streamhandler_logger
"""
Logging was used to print some messages, sent email or HTTP request to the specified address using 
this logging Module.
1. debug, info, warning, error, critical these are the types of logging we usually used in python.
2. How To create the Logger:
   1. import logging Module.
   2. using getLogger method and assign it to the variable.
   3. create handler.
   4. set the level for the handler.
   5. set the format for the handlers.
   6. add this handler to the logger (point 2) playing the role.
   7. finally use the handlers to log your messages.
"""
# import logging
log = logging.getLogger(__name__)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# set level for these handlers
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# make the format for this handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(messages)s')

# set the format for this handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

log.addHandler(stream_handler)
log.addHandler(file_handler)

log.warning("This is warning message")
log.error("This is error message")


try:
    a = 6 / 0
except Exception as e:
    custom_streamhandler_logger.stream_logger.error(f"Error is {e}", exc_info=True)