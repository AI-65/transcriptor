import sys
import os
from pydub import AudioSegment
from openai import OpenAI

import openai



def set_openai_key(key):
    openai.api_key = key
    return openai.api_key

def split_audio(file_path):
    """Splits the audio file into chunks of less than 25 MB each."""
    audio = AudioSegment.from_file(file_path)
    chunks = []
    chunk_length_ms = 10 * 60 * 1000  # 10 minutes in milliseconds

    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_name = f"{file_path}_part_{i // chunk_length_ms}.mp3"
        chunk.export(chunk_name, format="mp3")
        chunks.append(chunk_name)

    return chunks

def transcribe_audio(file_path):
    """Transcribes the audio file using OpenAI's Whisper model."""
    with open(file_path, "rb") as audio_file:
        transcript_response = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="text"
        )
    
    # Check the type of the response and extract text accordingly
    if isinstance(transcript_response, dict):
        # If the response is a dictionary, extract the text using the 'text' key
        return transcript_response.get('text', '')
    else:
        # If the response is a string, return it directly
        return transcript_response


def process_directory(directory):
    """Processes each audio file in the directory."""
    for filename in os.listdir(directory):
        if filename.endswith(('.mp3', '.wav')):
            file_path = os.path.join(directory, filename)
            file_size = os.path.getsize(file_path)

            if file_size > 25 * 1024 * 1024:  # 25 MB in bytes
                print(f"Splitting {filename}...")
                chunks = split_audio(file_path)
                full_transcript = ""
                for chunk in chunks:
                    transcript = transcribe_audio(chunk)
                    full_transcript += transcript
                    os.remove(chunk)  # Cleanup chunk file
                with open(f"{file_path}.txt", "w") as text_file:
                    text_file.write(full_transcript)
            else:
                transcript = transcribe_audio(file_path)
                with open(f"{file_path}.txt", "w") as text_file:
                    text_file.write(transcript)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: Directory does not exist.")
        sys.exit(1)

    process_directory(directory)
