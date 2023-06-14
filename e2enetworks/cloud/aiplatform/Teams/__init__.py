import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class Teams:
    @validate_access_key_and_token
    def create(self, team_name):
        payload = json.dumps({
            "team_name": team_name,
        })
        url = f"{BASE_GPU_URL}teams/?apikey={config.apikey}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def get(self, team_id):

        if type(team_id) != int:
            return f"Team ID - {team_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{team_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def list(self):
        url = f"{BASE_GPU_URL}teams/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def delete(self, team_id):

        if type(team_id) != int:
            return f"Team ID - {team_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{team_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()
