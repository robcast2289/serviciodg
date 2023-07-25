import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_name:str = os.getenv('DB_NAME_ORA')
    db_user:str = os.getenv('DB_USER_ORA')
    db_pass:str = os.getenv('DB_PASS_ORA')
    db_host:str = os.getenv('DB_HOST_ORA')
    db_port:int = os.getenv('DB_PORT_ORA')
    db_dns:str = os.getenv('DB_DNS_ORA')
    min_conns:int = os.getenv('DB_MIN_CONNS_ORA')
    max_conns:int = os.getenv('DB_MAX_CONNS_ORA')
    incr_conns:int = os.getenv('DB_INCR_CONNS_ORA')
    pool:str = os.getenv('DB_POOL_ORA')