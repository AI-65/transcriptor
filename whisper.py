from pathlib import Path
import openai
from config import load_configuration

# Load OpenAI API key from configuration
openai.api_key = load_configuration()

def speech_to_text(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            transcript_response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        # Debugging: Print the response type and content
        print("Response Type:", type(transcript_response))
        print("Raw Response:", transcript_response)

        # Extract text in a more robust manner
        if hasattr(transcript_response, 'text'):
            return transcript_response.text
        elif 'text' in transcript_response:
            return transcript_response['text']
        else:
            print("Transcription failed or text field missing in response")
            return None

    except Exception as e:
        print(f"Error in speech_to_text: {e}")
        return None

def write_transcript(file_path, transcript):
    txt_file_path = file_path.with_suffix('.txt')
    try:
        with open(txt_file_path, 'w') as f:
            f.write(transcript)
        print(f"Transcription saved to {txt_file_path}")
    except Exception as e:
        print(f"Error writing transcript to {txt_file_path}: {e}")

def main():
    audio_files_dir = input("Enter the folder path: ")
    file_format = input("Enter the preferred audio file format (e.g., mp3, wav): ")

    for file_path in Path(audio_files_dir).glob(f'*.{file_format}'):
        transcript = speech_to_text(file_path)
        print(f"Transcript received: {transcript}")  # Debugging print

        if transcript:
            write_transcript(file_path, transcript)
        else:
            print(f"Failed to transcribe {file_path}")

if __name__ == "__main__":
    main()
