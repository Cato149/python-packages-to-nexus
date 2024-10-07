import os
from dotenv import load_dotenv


load_dotenv(".")

PACKAGES_DIR = os.getenv('PACKAGES_DIR')
NEXUS_URL = os.getenv('NEXUS_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
