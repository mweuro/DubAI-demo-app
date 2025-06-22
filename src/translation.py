import deepl
import os
from typing import Optional

from dotenv import load_dotenv
load_dotenv()

class TranslationService:
    def __init__(self):
        self.translator = deepl.Translator(os.getenv("DEEPL_API_KEY"))

    def translate(
        self, 
        text: str, 
        source_lang: str = "PL",
        target_lang: str = "EN-US"
    ) -> str:
        """Tłumaczenie tekstu"""
        result = self.translator.translate_text(
            text, 
            source_lang=source_lang,
            target_lang=target_lang
        )
        return result.text

# Singleton pattern
TRANSLATOR = TranslationService()