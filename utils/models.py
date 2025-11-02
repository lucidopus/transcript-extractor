from pydantic import BaseModel
from typing import List, Dict, Any

class TranscriptRequest(BaseModel):
    url: str

class TranscriptResponse(BaseModel):
    transcript: List[Dict[str, Any]]