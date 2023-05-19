import json
import requests
from e2enetworks.constants import BASE_GPU_URL
from e2enetworks.cloud.aiplatform import config


class Projects:
    def __init__(self, team_id):
        self.team_id = team_id

    def create(self, project_name):
        payload = json.dumps({
            "project_name": project_name,
        })
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=4))

    def get(self, project_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def delete(self, project_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))
