import streamlit as st
import tempfile
import zipfile
import os
from streamlit_whisper import process_directory, set_openai_key

st.title("Audio Transcription Service")

# Prompt for OpenAI API Key
api_key = st.text_input("Enter your OpenAI API Key", type="password")
if api_key:
    set_openai_key(api_key)  # Function to set the API key in your transcription script

    uploaded_file = st.file_uploader("Upload audio files", accept_multiple_files=True)

    if uploaded_file:
        # Create a temporary directory to store the uploaded files
        with tempfile.TemporaryDirectory() as temp_dir:
            for file in uploaded_file:
                file_path = os.path.join(temp_dir, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())

            # Process the directory for transcription
            process_directory(temp_dir)

            # Zip the transcribed text files
            zip_name = "transcriptions.zip"
            with zipfile.ZipFile(zip_name, 'w') as zipf:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.txt'):
                            zipf.write(os.path.join(root, file), file)

            # Provide a link for downloading the zip file
            with open(zip_name, "rb") as f:
                st.download_button("Download Transcriptions", f, file_name=zip_name)

            # Cleanup
            os.remove(zip_name)
