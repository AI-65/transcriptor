import streamlit as st
import tempfile
import zipfile
import os
from streamlit_whisper import process_directory, set_openai_key

st.title("Audio Transcription Service")

# Input for OpenAI API Key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Button to set the API Key
if st.button("Set API Key"):
    if api_key:
        set_openai_key(api_key)  # Set the API key
        st.success("API Key set successfully!")
    else:
        st.error("Please enter a valid API Key.")

# Uploader for audio files
uploaded_files = st.file_uploader("Upload audio files", accept_multiple_files=True)

# Check if files are uploaded and API key is set
if uploaded_files and api_key:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the uploaded files to the temporary directory
        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Process the directory for transcription
        process_directory(temp_dir)

        # Zip the transcribed text files
        zip_name = "transcriptions.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    if file.endswith('.txt'):
                        zipf.write(os.path.join(root, file), os.path.basename(file))

        # Provide a link for downloading the zip file
        with open(zip_name, "rb") as f:
            st.download_button("Download Transcriptions", f, file_name=zip_name)

        # Cleanup
        os.remove(zip_name)
