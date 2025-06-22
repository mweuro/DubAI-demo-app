from TTS.api import TTS
import torch
from typing import Optional

class TTSService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self._load_model()

    def _load_model(self):
        """Ładowanie modelu XTTS v2"""
        return TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)

    def synthesize(
        self,
        text: str,
        reference_wav: str,
        output_path: str,
        language: str = "en"
    ) -> None:
        """Generacja pliku audio z tekstu"""
        self.model.tts_to_file(
            text=text,
            speaker_wav=reference_wav,
            language=language,
            file_path=output_path
        )

# Singleton pattern
XTTS = TTSService()