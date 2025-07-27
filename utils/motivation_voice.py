import os
import uuid
from gtts import gTTS
import streamlit as st

AUDIO_DIR = "data/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def play_voice(text):
    try:
        # Generate audio file
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)

        tts = gTTS(text)
        tts.save(filepath)

        # Streamlit audio player
        with st.spinner("🎧 Playing voice..."):
            audio_file = open(filepath, "rb")
            st.audio(audio_file.read(), format="audio/mp3")
    except Exception as e:
        st.error(f"❌ Voice generation failed: {e}")
