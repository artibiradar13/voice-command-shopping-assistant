import openai
import streamlit as st
import tempfile

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_voice_command(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return transcript.text
