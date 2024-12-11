import os
from typing import Literal

import dotenv
import requests


def get_headers(api_token: str) -> dict:
    """Generate headers for API requests."""
    return {
        "Authorization": f"token {api_token}"
    }


def get_sessions(base_url: str, user_name: str, api_token: str) -> dict:
    """Get the list of active sessions."""
    headers = get_headers(api_token)
    r = requests.get(f"{base_url}/user/{user_name}/api/sessions", headers=headers)
    r.raise_for_status()
    return r.json()


def get_content(base_url: str, user_name: str, path: str, api_token: str) -> dict:
    """Get the content of a file."""
    headers = get_headers(api_token)
    r = requests.get(f"{base_url}/user/{user_name}/api/contents/{path}", headers=headers)
    r.raise_for_status()
    return r.json()


def _save_content(
    base_url: str,
    user_name: str,
    path: str,
    content: dict,
    name: str,
    type: Literal["notebook", "file", "directory"],
    api_token: str,
    format: Literal["json", "text", "base64"] = "json",
) -> dict:
    """Save the content of a file."""
    headers = get_headers(api_token)
    r = requests.put(
        f"{base_url}/user/{user_name}/api/contents/{path}",
        headers=headers,
        json={
            "content": content,
            "format": format,
            "name": name,
            "path": path,
            "type": type,
        },
    )
    r.raise_for_status()
    return r.json()


def save_all_contents(base_url: str, user_name: str, api_token: str):
    """Save all files from active sessions."""
    try:
        sessions = get_sessions(base_url, user_name, api_token)
        for session in sessions:
            session_path = session["path"]
            content = get_content(base_url, user_name, session_path, api_token)
            # from pprint import pprint  # Debug
            # pprint(content)  # Debug
            _ = _save_content(
                base_url,
                user_name,
                session_path,
                content["content"],
                content["name"],
                content["type"],
                api_token,
            )
            # print(_)  # Debug
    except Exception as e:
        print(f"Error saving contents: {e}")


def shutdown_server(base_url: str, user_name: str, server_name: str, api_token: str):
    """Shutdown the server."""
    headers = get_headers(api_token)
    r = requests.delete(
        f"{base_url}/hub/api/users/{user_name}/servers/{server_name}", headers=headers
    )
    r.raise_for_status()


def start_server(base_url: str, user_name: str, server_name: str, api_token: str):
    """Start the server."""
    headers = get_headers(api_token)
    r = requests.post(
        f"{base_url}/hub/api/users/{user_name}/servers/{server_name}", headers=headers
    )
    r.raise_for_status()


def restart_server(base_url: str, user_name: str, server_name: str, api_token: str):
    """Restart the server."""
    # 
    # save_all_contents(base_url, user_name, api_token)
    shutdown_server(base_url, user_name, server_name, api_token)
    start_server(base_url, user_name, server_name, api_token)


# Example usage
if __name__ == "__main__":
    dotenv.load_dotenv()

    API_TOKEN = os.getenv("API_TOKEN")
    if not API_TOKEN:
        raise ValueError("API_TOKEN is not set in the environment variables.")

    BASE_URL = "http://127.0.0.1:8000"
    USER_NAME = "vscode"
    SERVER_NAME = ""

    # print(get_sessions(BASE_URL, USER_NAME, API_TOKEN))
    # print(get_content(BASE_URL, USER_NAME, "aaa.ipynb", API_TOKEN))
    # print(save_all_contents(BASE_URL, USER_NAME, API_TOKEN))

    # Example: Restart the server
    restart_server(BASE_URL, USER_NAME, SERVER_NAME, API_TOKEN)
