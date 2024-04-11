from dotenv import load_dotenv
import pyttsx3 as pt
import streamlit as st

# Load environment variables from .env file (if needed)
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title="Text Voice")

# Streamlit app header
st.header("Text To Speech")

# Text input widget for user input
molu = st.text_input("What do you want to convert to speech?: ", key="input")

# Button to trigger text-to-speech conversion
submit = st.button("Enter")

# Initialize pyttsx3 engine
text_speech = pt.init()

# Function to speak the given text with the selected voice
def speak_text(text, voice_id):
    # Set the voice for speech synthesis
    text_speech.setProperty('voice', voice_id)
    # Speak the provided text
    text_speech.say(text)
    text_speech.runAndWait()

# Voice selection options
voices = text_speech.getProperty('voices')

# Display voice selection buttons
voice_selection = st.radio("Select Voice:", [voice.name for voice in voices])

# Display the selected voice's details this code is showing only one option for voice add more options