import os
from configobj import ConfigObj
from pydantic_settings import BaseSettings, SettingsConfigDict

config = ConfigObj("config.ini")

class Settings(BaseSettings):
    DB_USER: str = config['database']['user']
    DB_PASSWORD: str = config['database']['password']
    DB_HOST: str = config['database']['host']
    DB_PORT: str = config['database']['port']
    DB_NAME: str = config['database']['postgres']['name']

    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )

    def get_db_url(self):
        return (f"sqlite+aiosqlite:///instance/{config['database']['sqlite']['name']}") # connection for local async sqlite db
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}") #connection for remote async postgres db
    
settings = Settings()
