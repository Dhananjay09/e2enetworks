import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class Models:
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
    def create(self, name, bucket_type, bucket_name, model_type):

        status, response = self.validate()

        if not status:
            return response

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
        # return response.json()

    @validate_access_key_and_token
    def get(self, model_id):

        status, response = self.validate()

        if not status:
            return response

        if type(model_id) != int:
            return f"Model ID - {model_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/{model_id}" \
              f"?apikey={config.apikey}"
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

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def delete(self, model_id):
        status, response = self.validate()

        if not status:
            return response

        if type(model_id) != int:
            return f"Model ID - {model_id} Should be Integer"

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/{model_id}/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()
