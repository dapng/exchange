from fastapi import FastAPI
from db.base import database
from endpoints import users, auth


app = FastAPI(title="API exchange")
app.include_router(users.router, prefix="/users", tags=["Users methods"])
app.include_router(auth.router, prefix="/auth", tags=["Auth method"])

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()