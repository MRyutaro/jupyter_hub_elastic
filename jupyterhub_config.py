# Configuration file for jupyterhub.

print("Hello Jupyter Hub Config")

c = get_config() # type: ignore

# http://localhost:8000
# にアクセスする

c.JupyterHub.active_server_limit = 3
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.JupyterHub.allow_named_servers = True
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.Spawner.default_url = '/lab'
c.Spawner.notebook_dir = '/workspaces/jupyter_hub_elastic'
c.Authenticator.allowed_users = set("vscode")
c.Authenticator.admin_users = set("vscode")
