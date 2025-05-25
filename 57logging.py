#Logging in Python
#Logging is the process of recording messages during the execution of a program to provide runtime information that can be useful for monitoring, debugging, and auditing.
import logging

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s -'
' %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')