import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile

# Load model only once
model = whisper.load_model("base")


def get_voice_command():

    fs = 16000
    seconds = 5

    print("Listening... Speak now")

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    # Save temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    wav.write(temp_file.name, fs, recording)

    print("Processing...")

    result = model.transcribe(temp_file.name)

    command = result["text"]

    print("You said:", command)

    return command.lower()