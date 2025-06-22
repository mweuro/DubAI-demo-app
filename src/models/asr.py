import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from typing import Optional
import torch


class ASRService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor, self.model = self._load_model()

    def _load_model(self):
        """Ładowanie modelu Whisper"""
        model_name = "openai/whisper-large-v3-turbo"
        processor = WhisperProcessor.from_pretrained(model_name)
        model = WhisperForConditionalGeneration.from_pretrained(model_name).to(self.device)
        model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language="pl", task="transcribe")
        return processor, model

    def transcribe(self, audio_path: str) -> str:
        """Transkrypcja audio na tekst"""
        sample, sr = librosa.load(audio_path, sr=16000)
        input_features = self.processor(
            sample, 
            sampling_rate=sr, 
            return_tensors="pt"
        ).input_features.to(self.device)
        
        predicted_ids = self.model.generate(input_features)
        return self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

# Singleton pattern
ASR = ASRService()