from .models import TranscriptRequest, TranscriptResponse
from .helper import get_transcript

def process_transcript(request: TranscriptRequest) -> TranscriptResponse:
    transcript = get_transcript(request.url)
    return TranscriptResponse(transcript=transcript)