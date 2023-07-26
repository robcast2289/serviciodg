import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_driver:str = os.getenv('DB_DRIVER_SQL')
    db_host:str = os.getenv('DB_HOST_SQL')
    db_name:str = os.getenv('DB_NAME_SQL')
    db_user:str = os.getenv('DB_USER_SQL')
    db_pass:str = os.getenv('DB_PASS_SQL')
    