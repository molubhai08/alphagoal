from dotenv import load_dotenv
import pyttsx3 as pt
import streamlit as st

# Load environment variables from .env file (if needed)
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title=" Voice Generator")

# Streamlit app header
st.header("Text To Speech")

# Text input widget for user input
text_input = st.text_input("What do you want to convert to speech?: ")

# Button to trigger text-to-speech conversion
submit = st.button("Convert to Speech")

# Initialize pyttsx3 engine
text_speech = pt.init()

# Function to speak the given text with the selected voice
def speak_text(text, voice_id):
    # Set the voice for speech synthesis
    text_speech.setProperty('voice', voice_id)
    # Speak the provided text
    text_speech.say(text)
    text_speech.runAndWait()

# Get available voices
voices = text_speech.getProperty('voices')

# Display voice selection options
voice_names = [voice.name for voice in voices]
selected_voice = st.selectbox("Select Voice:", voice_names)

# Find the voice ID based on the selected voice name
selected_voice_id = None
for voice in voices:
    if voice.name == selected_voice:
        selected_voice_id = voice.id
        break

# Perform text-to-speech conversion upon button click
if submit:
    if text_input:
        speak_text(text_input, selected_voice_id)
    else:
        st.warning("Please enter some text to convert to speech.")

selected_voice = next(voice for voice in voices if voice.name == voice_selection)
st.write(f"Selected Voice: {selected_voice.name}")

# Process button click event
if submit:
    speak_text(molu, selected_voice.id)
