# mint-nim
Minimal FastAPI app with two endpoints.

## Run
1) Create venv: `python3 -m venv .venv && source .venv/bin/activate`
2) Install deps: `python3 -m pip install -r requirements.txt`
3) Start: `python3 -m uvicorn app.main:app --reload --port 8080`
4) Try: open `http://127.0.0.1:8080/docs`

## Endpoints
- GET `/health` → `{"status":"ok"}`
- POST `/generate` → echoes prompt; accepts `max_tokens` (1–256)
