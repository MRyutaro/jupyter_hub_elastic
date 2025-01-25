import os
from typing import Literal

import dotenv
import requests


def get_headers(api_token: str) -> dict:
    """Generate headers for API requests."""
    return {
        "Authorization": f"token {api_token}"
    }


def get_kernels(base_url: str, user_name: str, api_token: str) -> dict:
    """Get the list of active kernels."""
    headers = get_headers(api_token)
    r = requests.get(f"{base_url}/user/{user_name}/api/kernels", headers=headers)
    r.raise_for_status()
    return r.json()


# Example usage
if __name__ == "__main__":
    dotenv.load_dotenv()

    API_TOKEN = os.getenv("API_TOKEN")
    if not API_TOKEN:
        raise ValueError("API_TOKEN is not set in the environment variables.")

    BASE_URL = "http://127.0.0.1:8000"
    USER_NAME = "vscode"
    SERVER_NAME = ""

    kernels = get_kernels(BASE_URL, USER_NAME, API_TOKEN)
    print(kernels)
