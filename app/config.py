import os

class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "models/")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")
    API_KEY = os.getenv("API_KEY", "default_api_key")
