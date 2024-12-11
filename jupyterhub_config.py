import os

import dotenv

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
if API_TOKEN is None:
    raise ValueError('API_TOKEN is not set')

print("Hello Jupyter Hub Config")

c = get_config() # type: ignore

# http://localhost:8000
# にアクセスする

c.JupyterHub.active_server_limit = 5

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

c.Authenticator.allowed_users = set(['vscode', 'user01', 'user02', 'user03'])
c.Authenticator.admin_users = set(['vscode'])
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = ''

c.JupyterHub.allow_named_servers = True
c.Spawner.default_url = '/lab'

c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

# REST APIを使うための設定
c.JupyterHub.api_tokens = {
    API_TOKEN: 'vscode'
}
"""
TODO: 
api_tokensは非推奨とのこと
以下のように書き換える
c.JupyterHub.services = [
    {
        # give the token a name
        "name": "service-admin",
        "api_token": "secret-token",
        # "admin": True, # if using JupyterHub 1.x
    },
]
c.JupyterHub.load_roles = [
    {
        "name": "service-role",
        "scopes": [
            # specify the permissions the token should have
            "admin:users",
        ],
        "services": [
            # assign the service the above permissions
            "service-admin",
        ],
    }
]
"""

# 隠しファイルを表示する
c.Spawner.args = [
    '--ContentsManager.allow_hidden=True',
]

# カスタムテンプレートのパスを設定
# c.JupyterHub.template_paths = ['./templates']
