import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION


class APITokens:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id

    def create(self, auth_token):
        payload = json.dumps({
            "auth_token": auth_token,
        })
        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/?apikey={config.apikey}&project_id={self.project_id}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/?apikey={config.apikey}&project_id={self.project_id}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))

    def delete(self, token_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/{token_id}/?apikey={config.apikey}&project_id=" \
              f"{self.project_id}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
