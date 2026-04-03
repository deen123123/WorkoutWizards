from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()

class Settings(BaseSettings):
    database_uri: str
    secret_key: str
    env: str
    api_key_exercise:str
    jwt_algorithm: str="HS256"
    jwt_access_token_expires:int=30
    app_host: str="0.0.0.0"
    app_port: int=8000
    db_pool_size:int=10
    db_additional_overflow:int=10
    db_pool_timeout:int=10
    db_pool_recycle:int=10
    
    model_config = SettingsConfigDict(env_file=".env")
