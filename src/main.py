from pathlib import Path
from fastapi import FastAPI, HTTPException
from model import Prompt
from config import get_prompt_prefix
from ollama import make_prompt_request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pymaker", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    indexHTMLText: str = Path("index.html").read_text()
    return HTMLResponse(
        content=indexHTMLText,
        status_code=200,
    )

@app.post("/prompt")
async def prompt(prompt: Prompt):
    maybe_response_stream = make_prompt_request(get_prompt_prefix() + prompt.promptText)
    if isinstance(maybe_response_stream, int):
        status_code = maybe_response_stream
        match status_code:
            case 404:
                errorMessage = "Model does not exist"
            case 400:
                errorMessage = "Bad request"
            case _:
                errorMessage = "Something happened"
        raise HTTPException(status_code, errorMessage)
    else:
        response_stream = maybe_response_stream
        return StreamingResponse((j["response"] for j in response_stream), media_type="text/plain")