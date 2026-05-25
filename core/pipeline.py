import json
import os
from core.llm_client import FactCheckerClient
from utils.logger import logger

class Pipeline:
    def __init__(self):
        self.llm_client = FactCheckerClient()
        self.templates = self._load_prompts()
        logger.debug("Pipeline initialized and templates loaded.")

    def _load_prompts(self) -> dict:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        template_path = os.path.join(base_dir, 'prompts', 'templates.json')
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def run(self, claim: str, language: str) -> dict:
        logger.info(f"Running pipeline in language: {language.upper()}")
        system_prompt = self.templates.get(language, self.templates["fa"])
        return self.llm_client.validate_claim(system_prompt, claim)