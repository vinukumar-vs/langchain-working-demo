from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

def getEnv(key):
    return os.getenv(key)