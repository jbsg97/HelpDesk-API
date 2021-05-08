from fastapi import FastAPI, Depends, HTTPException, status
from .api.v1.api import router as api_router
from .db.db import db
from .core.auth import oauth2_scheme
from .models.user import Token
from fastapi.security import OAuth2PasswordRequestForm
from .services.user import verify_user
from .core.auth import create_access_token
from datetime import timedelta
from .core.const import ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()

app.include_router(api_router, prefix="/v1")

@app.on_event("startup")
async def connect_db():
    await db.connect()

@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()
        
@app.get("/", tags=["Health Check"])
async def health_check():
    return {"message": "Api working fine.."}

@app.get("/login")
async def token(token: str = Depends(oauth2_scheme)):
    return {'Token': token}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
