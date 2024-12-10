"""
https://jupyterhub.readthedocs.io/en/stable/tutorial/server-api.html#stopping-servers
"""

import os
import requests
import dotenv
from pprint import pprint

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
if API_TOKEN is None:
    raise ValueError('API_TOKEN is not set')

api_url = 'http://127.0.0.1:8081/hub/api'

user_name = 'vscode'
server_name = '1'

r = requests.delete(
    api_url + f'/users/{user_name}/servers/{server_name}',
    headers={
        'Authorization': f'token {API_TOKEN}'
    }
)

r.raise_for_status()
