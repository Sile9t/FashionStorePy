import os
from pydantic_settings import BaseSettings, SettingsConfigDict

try:
    instancePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instance")
    os.makedirs(instancePath)
except OSError:
    pass

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )

    
    def get_db_url(self):
        return (f"sqlite+aiosqlite:///instance/db.sqlite3") # connection for local async sqlite db
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}") #connection for remote async postgres db
    
settings = Settings()
