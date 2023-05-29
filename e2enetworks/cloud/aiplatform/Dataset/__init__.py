import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION


class Datasets:
    def __init__(self, team_id, project_id):
        self.team_id = team_id
        self.project_id = project_id

    def create(self, bucket_name, bucket_type=None):
        pass

    def get(self, bucket_name):
        pass

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/" \
              f"eos-bucket-selection-list/?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))
        #return response.json()

    def delete(self, bucket_name):
        pass
