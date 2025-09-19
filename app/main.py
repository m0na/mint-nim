from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="mint-nim")

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = Field(default=64, ge=1, le=256)

class GenerateResponse(BaseModel):
    output: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    text = (req.prompt or "").strip() or "Hello from mint-nim"
    limit = req.max_tokens or 64
    clipped = text[:limit]  # simple stand-in for token limit
    return {"output": f"{clipped} ✨ (tokens={limit})"}