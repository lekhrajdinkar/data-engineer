# netstat -ano | findstr :8000
# taskkill /PID xxxx /F
from fastapi import FastAPI, Header, Query, Path, Body, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from fastapi.security import  OAuth2PasswordRequestForm
from src.webModule.controller.jwt_token_generator import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import  timedelta

from src.webModule.controller.okta_oauth import verify_okta_token, get_okta_token, request_token

# Ov23lil5yQRaFLoEzvu9 | b9cd5a1192bc6d7aa75fbec2642bc3f6dc613309

app = FastAPI(
    title="Python API doc",
    description="API for python POC",
    version="1.0.0",
    contact={
        "name": "Lekhraj Dinkar",
        "email": "LekhrajDinkarus@gmail.com",
    }
)



# Step 5: OAuth2 Password Flow + JWT
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "admin":
        access_token = create_access_token(
            data={"sub": form_data.username},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

# --- Step 1: Host Simple API ---
# @app.get("/")
# async def root():  return {"message": "Welcome to FastAPI!"}

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
        payload: dict = Body(None, description="Request body as a dictionary"),
        #token_payload: dict = Depends(verify_token),
        #gh_app: dict = Depends(verify_github_token)
        authorization: str = Header(...)
):
    all_header = dict(request.headers)
    all_qp = dict(request.query_params)

    token = authorization.removeprefix("Bearer ").strip()
    user_info = await verify_okta_token(token)

    return {
        "item_id": item_id,
        "query_param_1": q1, "query_param_2": q2,
        "header_1": h1,  "header_2": h2,
        "payload": payload,
        "all_header": all_header,
        "all_qp": all_qp,
        "user_info" : user_info
    }

@app.post("/okta/request-token")
async def okta_request_token():
    return request_token()