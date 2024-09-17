# video-transcriber
A simple python script that summarize videos using Whisper through OpenAI's API

### Prerequisites
- Python (latest) must be installed on your system
- You'll also need an OpenAI API key loaded with some credits ($10 dollars will last you a long time, especially if you're only transcribing shorts)

### How to use
1. Download ``transcribeVids.py`` and place it in the folder where you keep your videos
2. Edit it and paste in your OpenAI API key on line 24 (``client = OpenAI(api_key="<insert api key here>")``).
3. Run the script by double clicking it or running it in a terminal. The script will now transcribe all videos in the folder it is located in, outputting the transcripts as text files with the same names as the videos.

### Additional notes
- The script will not transcribe videos if a transcript for the video already exists in the folder.
- The model used for transcriptions is whisper-1. The cost per minute is currently $0.006 / minute (rounded to the nearest second), according to the [documentation](https://openai.com/api/pricing/)
- To further enhance your transcripts, you can also consier to use the [Hive ASR Dictionary](https://github.com/mp-hive/Hive-ASR-Dictionary) on your transcripts to scrub it for common spelling errors for various Hive-related terms.
