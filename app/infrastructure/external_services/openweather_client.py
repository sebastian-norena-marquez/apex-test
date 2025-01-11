import requests
from app.core.config import Config

class OpenWeatherClient:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.base_url = api_url

    def get_weather_by_city(self, city: str) -> dict:
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }

    def get_weather_by_coordinates(self, lat: float, lon: float) -> dict:
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
