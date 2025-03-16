from pydub import AudioSegment
import numpy as np

def remove_vocals(audio_path, output_path):
    audio = AudioSegment.from_file(audio_path)

    left_channel = audio.split_to_mono()[0]
    right_channel = audio.split_to_mono()[1]

    left_array = np.array(left_channel.get_array_of_samples())
    right_array = np.array(right_channel.get_array_of_samples())

    instrumental = AudioSegment(
        left_array - right_array,
        frame_rate=audio.frame_rate,
        sample_width=left_array.dtype.itemsize,
        channels=1
    )

    instrumental.export(output_path, format="wav")

input_audio_path = "D:\\RAMYA FOLDER\\B.TECH CSBS II YEAR\\SIH 2023\\input files\\extracted_audio.wav"
output_audio_path = "D:\\RAMYA FOLDER\\B.TECH CSBS II YEAR\\SIH 2023\\input files\\final.wav"

remove_vocals(input_audio_path, output_audio_path)
