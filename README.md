
# Audio Transcription Tool

## Overview
This Python-based tool is designed for transcribing recorded meetings, lectures, interviews, and other audio files. It leverages OpenAI's Whisper model to deliver accurate and efficient speech-to-text conversion. The script supports various audio formats, including mp3 and wav, allowing users to specify their preferred format.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup
Follow these steps to set up the tool:

1. Clone the repository:
   ```bash
   git clone [Your Repository URL]
   cd [Your Repository Name]
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
To use the transcription tool:

1. Navigate to the repository directory.
2. Run the script:
   ```bash
   python whisper.py
   ```
3. Enter the path to the folder containing the audio files when prompted.
4. Specify the preferred audio file format (e.g., mp3, wav).

The script will process and transcribe all audio files of the specified format in the given directory.

## Configuration
Ensure that you have created a `.env` file with your OpenAI API key as described in the Setup section. This is essential for the transcription service to function properly.

## Contributing
We welcome contributions! Feel free to fork the repository, make changes, and submit pull requests. For substantial changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)
