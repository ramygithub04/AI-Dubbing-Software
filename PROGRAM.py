import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

# Step 1: Video Processing
video = mp.VideoFileClip("20 Best English Stories For Kids Collection - english.mp4")
audio = video.audio

# Step 2: Speech Recognition
recognizer = sr.Recognizer()
with sr.AudioFile("extracted_audio.wav") as source:
    audio_text = recognizer.recognize_google(source)

# Step 3: Language Selection
target_language = input("Enter the target language for translation: ")

# Step 4: Translation
translator = Translator()
translated_text = translator.translate(audio_text, dest=target_language).text

# Step 5: Text-to-Speech (TTS) with Emotions (using a TTS library of your choice)

# Step 6: Audio File Generation
output_file = "output_audio.mp3"
tts = gTTS(translated_text, lang=target_language)
tts.save(output_file)
