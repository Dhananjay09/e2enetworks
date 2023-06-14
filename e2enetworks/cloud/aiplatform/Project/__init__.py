import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class Projects:
    def __init__(self, team_id):
        self.team_id = team_id
        self.validate()

    def validate(self):
        if type(self.team_id) != int:
            print(f"Team Id -{self.team_id} Should be Integer")
            return False, f"Team Id -{self.team_id}should be Integer"

    def clear_values(self):
        self.team_id = None

    @validate_access_key_and_token
    def create(self, project_name):

        status, response = self.validate()

        if not status:
            return response

        payload = json.dumps({
            "project_name": project_name,
        })

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def get(self, project_id):

        status, response = self.validate()

        if not status:
            return response

        if type(project_id) != int:
            return f"Project ID - {project_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def delete(self, project_id):

        status, response = self.validate()

        if not status:
            return response

        if type(project_id) != int:
            return f"Project ID - {project_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()
