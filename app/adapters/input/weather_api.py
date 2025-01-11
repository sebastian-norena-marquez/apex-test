from fastapi import APIRouter, Query, HTTPException, Depends
from app.infrastructure.external_services.openweather_client import OpenWeatherClient
from app.core.config import Config

router = APIRouter()
config = Config()
weather_client = OpenWeatherClient(api_key=config.OPENWEATHER_API_KEY, api_url=config.OPENWEATHER_API_URL)

@router.get("/")
async def get_weather(
    city: str = Query(None),
    lat: float = Query(None),
    lon: float = Query(None),
):
    if city:
        try:
            return weather_client.get_weather_by_city(city)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    elif lat is not None and lon is not None:
        try:
            return weather_client.get_weather_by_coordinates(lat, lon)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(
            status_code=400,
            detail="You must provide either 'city' or 'lat' and 'lon'.",
        )
