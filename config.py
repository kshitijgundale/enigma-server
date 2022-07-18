import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    MONGO_URL = os.environ.get("MONGO_URL")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")