import os
from dotenv import load_dotenv

load_dotenv()


TARGET_FOLDER_NAME = os.getenv('TARGET_FOLDER_NAME')
USERNAME = os.getenv('USERNAME')
PORT = os.getenv('PORT')
SERVER_NAME = os.getenv('SERVER_NAME')
FROM_ADDR = os.getenv('FROM_ADDR')
TO_ADDR = os.getenv('TO_ADDR')
CONNECTION_SECURITY = os.getenv('CONNECTION_SECURITY', 'STARTTLS')
PASSWORD = os.getenv('PASSWORD')