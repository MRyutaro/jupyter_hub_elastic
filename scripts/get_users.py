import os
from pprint import pprint

import dotenv
import requests

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
if API_TOKEN is None:
    raise ValueError('API_TOKEN is not set')

api_url = 'http://127.0.0.1:8081/hub/api'

r = requests.get(api_url + '/users',
    headers={
        'Authorization': f'token {API_TOKEN}'
    }
)

r.raise_for_status()
users = r.json()
pprint(users)
