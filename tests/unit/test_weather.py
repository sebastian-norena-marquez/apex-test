from unittest.mock import Mock
from app.infrastructure.external_services.openweather_client import OpenWeatherClient
import pytest

mock_client = Mock()
weather_service = OpenWeatherClient(
    api_key="test_key",
    api_url="https://api.openweathermap.org/data/2.5/weather"
)

@pytest.fixture
def mock_requests_get(monkeypatch):
    def mock_get(*args, **kwargs):
        return Mock(
            status_code=200,
            json=lambda: {
                "main": {"temp": 20.0},
                "weather": [{"description": "clear sky"}],
            },
        )
    monkeypatch.setattr("requests.get", mock_get)

def test_get_weather_by_city(mock_requests_get):
    result = weather_service.get_weather_by_city("London")
    assert result["temperature"] == 20.0

def test_get_weather_by_coordinates(mock_requests_get):
    result = weather_service.get_weather_by_coordinates(51.5074, -0.1278)
    assert result["temperature"] == 20.0
