from fastapi import FastAPI, APIRouter
from router.estancia import estancia
import requests
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.on_event("startup") # Use on_event to start after FastAPI
def start_background_tasks():
    scheduler = BackgroundScheduler()
    scheduler.add_job(keep_awake, 'interval', minutes=8) # trigger every 8 minutes
    scheduler.start()
def keep_awake():
    try:
        response = requests.get("http://127.0.0.1:8000/")  # Ping your root endpoint
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(f"Ping successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ping failed: {e}")

app.include_router(estancia)
