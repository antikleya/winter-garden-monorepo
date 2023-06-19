from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_SYNC_URL = os.environ['DATABASE_SYNC_URL']
DATABASE_ASYNC_URL = os.environ['DATABASE_ASYNC_URL']
JWT_TOKEN = os.environ['JWT_TOKEN']
PASSWORD_VERIFICATION_TOKEN = os.environ['PASSWORD_VERIFY_TOKEN']
ACCESS_HEADER = os.environ['ACCESS_HEADER_VALUE']
TZ = os.environ['TZ']
MIN_TARGET_TEMP = 15
MAX_TARGET_TEMP = 25
MIN_PUMP_TEMPERATURE_DELTA = -10
MAX_PUMP_TEMPERATURE_DELTA = 10
MAX_TARGET_HUMIDITY = 60