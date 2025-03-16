from pydub import AudioSegment

# Specify the path to the FFmpeg executable
AudioSegment.ffmpeg = r"C:\Users\F2H\Downloads\ffmpeg-6.0.tar.xz"

# Now, you can use Pydub as usual
audio = AudioSegment.from_file("input_audio.mp3")
# Perform audio processing here

# Export the result
audio.export("output_audio.wav", format="wav")
