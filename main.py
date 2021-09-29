from fastapi import FastAPI
from db.base import database

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Test"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()