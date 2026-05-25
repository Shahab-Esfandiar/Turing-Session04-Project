import logging
import os

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure the custom logger
logger = logging.getLogger("FactCheckerApp")
logger.setLevel(logging.DEBUG)

# Format for the logs
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 1. Console Handler (Prints to Terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 2. File Handler (Saves to file)
file_handler = logging.FileHandler('logs/app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers to the logger
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)