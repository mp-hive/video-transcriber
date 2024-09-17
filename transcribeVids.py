import sys
import subprocess
import pkg_resources

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required = {'openai', 'moviepy'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing missing packages...")
    for package in missing:
        print(f"Installing {package}...")
        install(package)
    print("All required packages installed successfully.")

import os
from openai import OpenAI
from moviepy.editor import VideoFileClip

# Initialize OpenAI client
client = OpenAI(api_key="<insert api key here>")

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcription.text

def process_videos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith((".mp4", ".avi", ".mov")):  # Add more video formats if needed
            video_path = os.path.join(folder_path, filename)
            transcript_path = os.path.splitext(video_path)[0] + ".txt"
            
            if not os.path.exists(transcript_path):
                print(f"Processing {filename}...")
                
                # Extract audio
                audio_path = os.path.splitext(video_path)[0] + ".mp3"
                extract_audio(video_path, audio_path)
                
                # Transcribe audio
                transcript = transcribe_audio(audio_path)
                
                # Save transcript
                with open(transcript_path, "w", encoding="utf-8") as f:
                    f.write(transcript)
                
                # Remove temporary audio file
                os.remove(audio_path)
                
                print(f"Transcription saved for {filename}")
            else:
                print(f"Transcript already exists for {filename}")

if __name__ == "__main__":
    folder_path = os.path.dirname(os.path.abspath(__file__))
    process_videos(folder_path)
    
    print("All videos processed. Press Enter to exit.")
    input()