from fastapi import FastAPI
from .api.v1.api import router as api_router
from .db.db import db

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
