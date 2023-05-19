import json
import requests
from e2enetworks.constants import BASE_GPU_URL
from e2enetworks.cloud.aiplatform import config


class EndPoint:
    def __init__(self, model):
        self.model = model

    def create(self, model_id, sku_id, storage_url, replica):
        payload = json.dumps({
            "sku_id": sku_id,
            "storage_url": storage_url,
            "replica": replica
        })
        url = f"{BASE_GPU_URL}teams/{self.model.team_id}/projects/{self.model.project_id}/model/{model_id}/inference/" \
              f"?apikey={config.apikey}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=4))

    def get(self, model_id, endpoint_id):
        url = f"{BASE_GPU_URL}teams/{self.model.team_id}/projects/{self.model.project_id}/model/{model_id}/" \
              f"inference/{endpoint_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.model.team_id}/projects/{self.model.project_id}/model/inferences-list" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))

    def delete(self, model_id, endpoint_id):
        url = f"{BASE_GPU_URL}teams/{self.model.team_id}/projects/{self.model.project_id}/model/{model_id}/" \
              f"inference/{endpoint_id}/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=4))
