import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

AVALAI_API_KEY = os.getenv("AVALAI_API_KEY")
AVALAI_BASE_URL = os.getenv("AVALAI_BASE_URL", "https://api.avalai.ir/v1")
AVALAI_MODEL = os.getenv("AVALAI_MODEL", "gpt-5.4")

# Ensure critical API Key is present
if not AVALAI_API_KEY:
    raise ValueError("API Key is missing. Please check your .env file and ensure AVALAI_API_KEY is set.")