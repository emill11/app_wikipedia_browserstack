import os
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv('LOGIN')
access_key = os.getenv('PASSWORD')
url = os.getenv('URL')
time_out = float(os.getenv('TIMEOUT'))
