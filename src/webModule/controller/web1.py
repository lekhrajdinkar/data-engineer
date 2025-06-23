from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, status, Header
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from typing import Optional
import aiofiles
import os

app = FastAPI(title="web1 API")

# --- Rate Limiter ---
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# --- OAuth2 Password Bearer ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy token validation
async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "secrettoken":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"user": "demo_user"}

# --- Upload Endpoint ---
@app.post("/upload", dependencies=[Depends(get_current_user)])
@limiter.limit("5/minute")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    os.makedirs("files", exist_ok=True)
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return {"filename": file.filename, "status": "uploaded"}

# --- Download Endpoint with Progress ---
@app.get("/download/{filename}", dependencies=[Depends(get_current_user)])
@limiter.limit("10/minute")
async def download_file(filename: str):
    file_path = f"files/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    async def file_stream():
        async with aiofiles.open(file_path, 'rb') as f:
            chunk = await f.read(1024 * 1024)  # 1MB chunks
            while chunk:
                yield chunk
                chunk = await f.read(1024 * 1024)

    return StreamingResponse(file_stream(), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})

# --- Cached Metadata Endpoint ---
@app.get("/file-metadata/{filename}")
@limiter.limit("20/minute")
@cache(expire=60)
async def file_metadata(filename: str):
    file_path = f"files/{filename}"
    size = os.path.getsize(file_path) if os.path.exists(file_path) else None
    return {"filename": filename, "size": size}

# --- Custom Response Example ---
@app.get("/custom-response")
async def custom():
    return JSONResponse(status_code=202, content={"message": "Accepted"}, headers={"X-Custom": "Value"})

# --- Cache Init ---
@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="my-cache")

"""
next
Switch to Redis for caching
Add JWT login
Dockerize the app
Connect to PostgreSQL with SQLAlchemy
"""