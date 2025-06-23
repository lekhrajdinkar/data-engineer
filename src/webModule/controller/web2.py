# netstat -ano | findstr :8000
# taskkill /PID xxxx /F
from fastapi import FastAPI, Header, Query, Path, Body, Request
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI(
    title="Python API doc",
    description="API for python POC",
    version="1.0.0",
    contact={
        "name": "Lekhraj Dinkar",
        "email": "LekhrajDinkarus@gmail.com",
    }
)


# --- Step 1: Host Simple API ---
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

# --- Step 2: Custom JSON Response ---
@app.get("/custom-response")
async def custom_response():
    data = {
        "status": "Accepted",
        "note": "This is a custom response."
    }
    headers = {
        "X-My-Header": "CustomHeaderValue"
    }
    return JSONResponse(status_code=202, content=data, headers=headers)

# --- Step 3: Path, Query, Header, and Body Parameters ---
"""
item_id is a path parameter extracted from the URL path (e.g., /items/{item_id}).
... vs None ==== mandatory vs optional
Path(...) means this parameter is required.
Body(...) required
"""
@app.post("/items/{item_id}")
async def handle_params(
        request: Request,
        item_id: int = Path(..., description="The ID of the item (required)"),
        q1: Optional[str] = Query(..., description="Query string parameter (required str)"),
        q2: Optional[int] = Query(None, description="Query string parameter (optional int)"),
        h1: Optional[str] = Header(..., description="header (required str)"),
        h2: Optional[int] = Header(None, description="header (optional int)"),
        payload: dict = Body(..., description="Request body as a dictionary")
):
    all_header = dict(request.headers)
    all_qp = dict(request.query_params)

    return {
        "item_id": item_id,
        "query_param_1": q1, "query_param_2": q2,
        "header_1": h1,  "header_2": h2,
        "payload": payload,
        "all_header": all_header,
        "all_qp": all_qp
    }
