import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime

# Create logger
logger = logging.getLogger("agent_logger")
logger.setLevel(logging.INFO)

# Create file handler
handler = logging.FileHandler("agent_logs.json")

# Set JSON format
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def log_interaction(query: str, result: str):
    logger.info("interaction", extra={
        "query": query,
        "result": result,
        "timestamp": datetime.now().isoformat()
    })
