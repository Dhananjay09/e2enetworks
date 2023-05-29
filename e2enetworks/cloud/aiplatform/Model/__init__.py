import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION


class Models:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id

    def create(self, name, bucket_type, bucket_name, model_type):
        payload = json.dumps({
            "name": name,
            "type": bucket_type,
            "bucket_name": bucket_name,
            "model_type": model_type
        })
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/" \
              f"?apikey={config.apikey}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))
        ##return response.json()

    def get(self, model_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/{model_id}" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        #return response.json()

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        #return response.json()

    def delete(self, model_id):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/{model_id}/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        #return response.json()
