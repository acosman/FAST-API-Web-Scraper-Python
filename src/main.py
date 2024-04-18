from fastapi import FastAPI
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import services as _service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to this historical events API - cool eh?"}

@app.get("/events")
async def all_events():
    return _service.get_all_events()

@app.get("/events/{month}")
async def get_events_of_month(month: str):
    return _service.get_month_events(month)
