
import logging

# Create a custom logger

logging.basicConfig(
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
)


# creating an object of the logger

logger = logging.getLogger()

# setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# logging messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')