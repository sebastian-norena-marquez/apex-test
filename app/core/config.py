from pydantic import BaseSettings

class Config(BaseSettings):
    DATABASE_URL: str = "mongodb://mongo:27017"
    DATABASE_NAME: str = "product_db"
    OPENWEATHER_API_KEY: str
    OPENWEATHER_API_URL: str

    class Config:
        env_file = ".env"