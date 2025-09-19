from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import time
from fastapi import Request

app = FastAPI(title="mint-nim")

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = Field(default=64, ge=1, le=256)

class GenerateResponse(BaseModel):
    output: str


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    dur_ms = int((time.time() - start) * 1000)
    print(f"{request.method} {request.url.path} -> {response.status_code} ({dur_ms}ms)")
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    text = (req.prompt or "").strip() or "Hello from mint-nim"
    limit = req.max_tokens or 64
    clipped = text[:limit]  # simple stand-in for token limit
    return {"output": f"{clipped} ✨ (tokens={limit})"}

@app.get("/metrics")
def metrics():
    return {"ok": True}