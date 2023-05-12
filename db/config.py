import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

CONNECT = psycopg2.connect(f'{os.getenv("DATABASE_CONECTION")}')
OPERATIONAL_ERROR = psycopg2.OperationalError
