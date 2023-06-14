import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class Notebooks:
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
        return True, "Success"

    def clear_values(self):
        self.team_id = None
        self.project_id = None

    @validate_access_key_and_token
    def create(self, name, sku_id, image_id, instance_type):
        status, response = self.validate()

        if not status:
            return response

        payload = json.dumps({
            "name": name,
            "image_id": image_id,
            "sku_id": sku_id,
            "instance_type": instance_type
        })
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/" \
              f"?apikey={config.apikey}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))

    @validate_access_key_and_token
    def get(self, notebook_id):

        status, response = self.validate()

        if not status:
            return response

        if type(notebook_id) != int:
            print(f"Notebook ID - {notebook_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/{notebook_id}/?" \
              f"apikey={config.apikey}"
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

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def delete(self, notebook_id):

        status, response = self.validate()

        if not status:
            return response

        if type(notebook_id) != int:
            print(f"Notebook ID - {notebook_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/{notebook_id}/?" \
              f"apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def stop(self, notebook_id):

        status, response = self.validate()

        if not status:
            return response

        if type(notebook_id) != int:
            print(f"Notebook ID - {notebook_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/{notebook_id}/actions/" \
              f"?action=stop&apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def start(self, notebook_id):

        status, response = self.validate()

        if not status:
            return response

        if type(notebook_id) != int:
            print(f"Notebook ID - {notebook_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/{notebook_id}/actions/" \
              f"?action=start&apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    def upgrade(self, notebook_id, size):
        status, response = self.validate()

        if not status:
            return response

        if type(notebook_id) != int:
            print(f"Notebook ID - {notebook_id} Should be Integer")
            return

        if type(size) != int:
            print(f"Size - {size} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/notebooks/{notebook_id}/pvc/" \
              f"upgrade/?apikey={config.apikey}"
        payload = json.dumps({
            "size": size
        })
        headers = {
            'Authorization': f'Bearer {config.auth_token}',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://gpu-notebooks.e2enetworks.com',
            'Referer': 'https://gpu-notebooks.e2enetworks.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @staticmethod
    def help():
        help_text = """
                Notebooks class provides methods to interact with notebooks in a project.

                Available methods:
                1. create(name, sku_id, image_id, instance_type): Create a new notebook.
                2. get(notebook_id): Get information about a notebook.
                3. list(): List all notebooks in the project.
                4. delete(notebook_id): Delete a notebook.
                5. stop(notebook_id): Stop a running notebook.
                6. start(notebook_id): Start a stopped notebook.
                7. upgrade(notebook_id, size): Upgrade the size of a notebook's PVC.

                Usage:
                notebooks = Notebooks(team_id, project_id)
                notebooks.create(name, sku_id, image_id, instance_type)
                notebooks.get(notebook_id)
                notebooks.list()
                notebooks.delete(notebook_id)
                notebooks.stop(notebook_id)
                notebooks.start(notebook_id)
                notebooks.upgrade(notebook_id, size)
                """
        print(help_text)
