import struct

def extract_audio_from_avi(input_video_path, output_audio_path):
    # Read the AVI file
    with open(input_video_path, 'rb') as avi_file:
        avi_data = avi_file.read()

    # Find the 'strh' chunk, which contains audio stream information
    strh_offset = avi_data.find(b'strh')
    if strh_offset == -1:
        print("No 'strh' chunk found.")
        return

    # Find the audio stream type (0x73646976 is 'vids' in little-endian)
    stream_type = avi_data[strh_offset + 8:strh_offset + 12]
    if stream_type != b'auds':
        print("No audio stream found.")
        return

    # Find the 'strf' chunk, which contains audio format information
    strf_offset = avi_data.find(b'strf', strh_offset)
    if strf_offset == -1:
        print("No 'strf' chunk found.")
        return

    # Extract audio format data (e.g., sample rate, bits per sample)
    audio_format_data = avi_data[strf_offset + 8:strf_offset + 40]
    sample_rate, bits_per_sample = struct.unpack('<IHHIIII', audio_format_data)[0:2]

    # Find the 'strn' chunk, which contains audio stream name
    strn_offset = avi_data.find(b'strn', strh_offset)
    if strn_offset == -1:
        print("No 'strn' chunk found.")
        return

    # Extract audio stream name
    audio_stream_name = avi_data[strn_offset + 8:strn_offset + 12]

    # Find the 'strd' chunk, which contains audio data
    strd_offset = avi_data.find(b'strd', strh_offset)
    if strd_offset == -1:
        print("No 'strd' chunk found.")
        return

    # Extract audio data
    audio_data = avi_data[strd_offset + 8:]

    # Write the audio data to a WAV file
    with open(output_audio_path, 'wb') as audio_file:
        # WAV header
        audio_file.write(b'RIFF')
        audio_file.write(struct.pack('<I', len(audio_data) + 36))
        audio_file.write(b'WAVEfmt ')
        audio_file.write(struct.pack('<IHHII', 16, 1, 1, sample_rate, sample_rate * bits_per_sample // 8))
        audio_file.write(b'data')
        audio_file.write(struct.pack('<I', len(audio_data)))

        # Audio data
        audio_file.write(audio_data)

    print(f'Audio extracted and saved to {output_audio_path}')

input_video_path = 'C:\\Users\\F2H\\Downloads\\story.avi'
output_audio_path = 'C:\\Users\\F2H\\Downloads\\output_audio.wav'
extract_audio_from_avi(input_video_path, output_audio_path)
