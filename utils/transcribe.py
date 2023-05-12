import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import whisper

def transcribe(wave_output_file: str):
    model = whisper.load_model("base")
    res = model.transcribe(wave_output_file)
    output = (res['text'] or "").strip()
    return output
