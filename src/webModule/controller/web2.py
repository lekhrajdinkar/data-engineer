from fastapi import FastAPI

app = FastAPI(title="Simple API")

# --- Step 1: Host Simple API ---
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}