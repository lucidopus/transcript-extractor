from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

def get_transcript(url: str) -> list:
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi().fetch(video_id)
    return transcript.to_raw_data()