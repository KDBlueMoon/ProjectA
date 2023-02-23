from fastapi import FastAPI, Depends, APIRouter
from router import api
from sql_app.database import db_state_default, db
import psycopg2

app = FastAPI()


@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()


@app.on_event('shutdown')
def shutdown():
    if not db.is_closed():
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api.router)