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
server_name = ''

# サーバーの停止
r = requests.delete(
    f'{api_url}/users/{user_name}/servers/{server_name}',
    headers={
        'Authorization': f'token {API_TOKEN}'
    }
)

r.raise_for_status()
# 戻り値はない

# サーバーの再起動
r = requests.post(
    f'{api_url}/users/{user_name}/servers/{server_name}',
    headers={
        'Authorization': f'token {API_TOKEN}'
    }
)

r.raise_for_status()
# 戻り値はない
