"""
Logger Module: Configures A logger instance which logs files of whole scraper
"""


import logging
from src.configs.config import LOG_FILE


#! Basic Configuration
logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename=LOG_FILE,
    format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
)


#^ Logger instance
logger = logging.getLogger(__name__)
