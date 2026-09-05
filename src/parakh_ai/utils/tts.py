from gtts import gTTS
from io import BytesIO

def text_to_speech(text: str) -> BytesIO:
    """Convert text to speech and return raw mp3 bytes in memory (no disk write)."""
    tts = gTTS(text=text, lang="en")
    buffer = BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)
    return buffer