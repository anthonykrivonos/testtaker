import os

from utils.record import create_stream, watch_until_keypress, save_file
from utils.transcribe import transcribe
from typing import Callable
import warnings

FILENAME = "temp.wav"

def run_testtaker(solver: Callable[[str], str]):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            while True:
                print("✨ Press any key to start recording (Ctrl+C to exit)")
                input()
                print("🔴 Press Ctrl+C to stop recording")

                st = create_stream()

                frames = watch_until_keypress(st)
                print(f"📄 Done. Transcribing...")

                save_file(FILENAME, frames)
                transcription = transcribe(FILENAME)
                print(f"🎤 Got speech: {transcription}")

                solution = solver(transcription)
                print(f"✅Solution:\n{solution}")
        except KeyboardInterrupt:
            if os.path.exists(FILENAME):
                os.remove(FILENAME)
