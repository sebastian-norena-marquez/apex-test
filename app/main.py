from fastapi import FastAPI
from app.adapters.input.api import router as api_router
from app.adapters.input.weather_api import router as weather_router
app = FastAPI()

app.include_router(api_router)
app.include_router(weather_router, prefix="/weather", tags=["Weather"])