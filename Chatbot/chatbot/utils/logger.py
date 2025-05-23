import logging

# Basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("chatbot")

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)
