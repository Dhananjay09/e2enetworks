import json
import requests
from e2enetworks.constants import BASE_GPU_URL
from e2enetworks.cloud.aiplatform import config


class EndPoint:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id

    def create(self, name, sku_id, prefix, replica, model_id):
        payload = json.dumps({
            "name": name,
            "sku_id": sku_id,
            "prefix": prefix,
            "replica": replica,
            "model_id": model_id
        })
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/" \
              f"?apikey={config.apikey}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=4))

    def get(self, endpoint_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/?" \
              f"apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def delete(self, endpoint_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))
