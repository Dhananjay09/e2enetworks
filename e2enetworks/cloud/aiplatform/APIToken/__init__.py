import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class APITokens:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id
        self.validate()

    def validate(self):
        if type(self.team_id) != int:
            print(f"Team Id -{self.team_id} Should be Integer")
            return False, f"Team Id -{self.team_id}should be Integer"
        if type(self.project_id) != int:
            print(f"Project Id -{self.project_id} Should be Integer")
            return False, f"Project Id -{self.project_id} should be Integer"

    def clear_values(self):
        self.team_id = None
        self.project_id = None

    @validate_access_key_and_token
    def create(self, auth_token):

        status, response = self.validate()

        if not status:
            return response

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

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/?apikey={config.apikey}&project_id={self.project_id}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))

    @validate_access_key_and_token
    def delete(self, token_id):

        status, response = self.validate()

        if not status:
            return response

        if type(token_id) != int:
            return f"Token ID - {token_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/{token_id}/?apikey={config.apikey}&project_id=" \
              f"{self.project_id}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
