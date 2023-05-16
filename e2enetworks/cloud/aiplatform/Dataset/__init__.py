import requests
from e2enetworks.constants import BASE_GPU_URL


class Dataset:
    def __init__(self, team_id, project_id, credentials):
        self.team_id = team_id
        self.project_id = project_id
        self.credentials = credentials

    def create(self, bucket_name, bucket_type=None):
        pass

    def get(self, bucket_name):
        pass

    def list(self):
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/" \
              f"eos-bucket-selection-list/?apikey={self.credentials.access_key}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {self.credentials.api_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json()['data'])

    def delete(self, bucket_name):
        pass
