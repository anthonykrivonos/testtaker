import pyaudio
import wave
import sounddevice as sd
import atexit

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 16
fs = 44100  # Record at 44100 samples per second

p = pyaudio.PyAudio()

def exit_handler():
    p.terminate()

atexit.register(exit_handler)

def create_stream() -> pyaudio.Stream:
    sound_device_idx = [dev for dev in list(sd.query_devices()) if "blackhole" in dev["name"].lower()][0]["index"]
    return p.open(format=sample_format,
                  channels=channels,
                  rate=fs,
                  frames_per_buffer=chunk,
                  input_device_index=sound_device_idx,
                  input=True)

def watch_until_keypress(stream: pyaudio.Stream):
    frames = []
    index = 0
    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
            index += 1
    except KeyboardInterrupt:
        stream.stop_stream()
        stream.close()

    return frames

def save_file(filename: str, frames: bytes):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
