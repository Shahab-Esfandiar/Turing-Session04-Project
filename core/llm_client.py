import json
import requests
from config.settings import AVALAI_API_KEY, AVALAI_BASE_URL, AVALAI_MODEL
from utils.logger import logger

class FactCheckerClient:
    def __init__(self):
        self.api_key = AVALAI_API_KEY
        self.endpoint = f"{AVALAI_BASE_URL.rstrip('/')}/responses"
        logger.debug(f"FactCheckerClient initialized. Model: {AVALAI_MODEL}, Endpoint: {self.endpoint}")

    def validate_claim(self, system_prompt: str, user_claim: str) -> dict:
        logger.info(f"Starting validation for claim: '{user_claim[:50]}...'")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": AVALAI_MODEL,
            "instructions": system_prompt,
            "input": f"Claim/ادعا: {user_claim}",
            "tools": [{"type": "web_search"}],
            "text": {
                "format": "json_object"
            }
        }

        try:
            logger.debug("Sending POST request to AvalAI API...")
            response = requests.post(self.endpoint, headers=headers, json=payload)
            
            if response.status_code != 200:
                err_msg = f"API Error {response.status_code}: {response.text}"
                logger.error(err_msg)
                return {"error": err_msg}
                
            response_data = response.json()
            raw_output = response_data.get("output", "")
            
            if not raw_output:
                err_msg = "Empty response received from the advanced model endpoint."
                logger.warning(err_msg)
                return {"error": err_msg}
                
            logger.info("Validation completed successfully.")
            return json.loads(raw_output)
            
        except Exception as e:
            logger.error(f"Unexpected error during validation: {str(e)}")
            return {"error": str(e)}