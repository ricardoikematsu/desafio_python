import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql://user:password@mysql/previsao_tempo_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", "3994b23ce3182e20d5bce5a6f9ca8896")