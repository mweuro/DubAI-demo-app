from src.models.tts.xtts import XTTS
from src.models.asr import ASR
from src.models.translation import TRANSLATOR
import os
OUTPUT_WAV_PATH = "output.wav"


def PIPELINE(audio_file: str) -> str:
    # TRANSCRIPTION
    transcript = ASR.transcribe(audio_file)
    # TRANSLATION
    translation = TRANSLATOR.translate(transcript, source_lang="pl", target_lang="EN")
    # SYNTHESIS
    if os.path.exists(OUTPUT_WAV_PATH):
        os.remove(OUTPUT_WAV_PATH)
    XTTS.synthesize(
        text=translation,
        reference_wav=audio_file,
        output_path=OUTPUT_WAV_PATH,
        language="en"
    )

    return OUTPUT_WAV_PATH