import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
r = sr.Recognizer()

# Load the video's audio (replace 'video_audio.wav' with your video's audio file)
audio_path = r'C:\Users\F2H\Downloads\story.wav'

# Use the recognizer to transcribe the audio
with sr.AudioFile(audio_path) as source:
    audio = r.record(source)

try:
    # Recognize the speech using Google Web Speech API
    text = r.recognize_google(audio)
    
    # Display the recognized text
    print("Recognized Text:")
    print(text)
    
    # Convert the recognized text to speech and save it to an audio file
    tts = gTTS(text)
    tts.save('recognized_text.mp3')
    
    # Play the saved audio
    os.system("mpg321 recognized_text.mp3")  # This command plays the audio using mpg321 (Linux)
    
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
