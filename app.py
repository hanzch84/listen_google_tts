import streamlit as st
from google.cloud import texttospeech
import os

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

# Initialize TTS client
client = texttospeech.TextToSpeechClient()

def text_to_speech(text, language_code='en-US', voice_name='en-US-Wavenet-D'):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    
    return response.audio_content

# Streamlit app
st.title('Text-to-Speech with Google Cloud')

text_input = st.text_area('Enter text to convert to speech:')
language = st.selectbox('Select language:', ['en-US', 'es-ES', 'fr-FR', 'de-DE'])

if st.button('Generate Speech'):
    if text_input:
        audio = text_to_speech(text_input, language_code=language)
        st.audio(audio, format='audio/mp3')
    else:
        st.warning('Please enter some text.')
