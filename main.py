from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from utils.pipeline import process_transcript
from utils.models import TranscriptRequest

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/transcript")
async def get_transcript_endpoint(request: TranscriptRequest):
    try:
        response = process_transcript(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))