import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token


class EndPoints:
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
    def create(self, name, sku_id, prefix, replica, model_id):

        status, response = self.validate()

        if not status:
            return response

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
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(json.dumps(response.json(), indent=INDENTATION))

    @validate_access_key_and_token
    def get(self, endpoint_id):

        status, response = self.validate()

        if not status:
            return response

        if type(endpoint_id) != int:
            print(f"EndPoint ID - {endpoint_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/?" \
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

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def delete(self, endpoint_id):

        status, response = self.validate()

        if not status:
            return response

        if type(endpoint_id) != int:
            print(f"EndPoint ID - {endpoint_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/" \
              f"?apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))
        # return response.json()

    @validate_access_key_and_token
    def logs(self, endpoint_id):

        status, response = self.validate()

        if not status:
            return response

        if type(endpoint_id) != int:
            print(f"EndPoint ID - {endpoint_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/logs?" \
              f"apikey={config.apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {config.auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.dumps(response.json(), indent=INDENTATION))

    @staticmethod
    def help():
        print("EndPoint Class Help")
        print("=================")
        print("This class provides functionalities to interact with EndPoint.")
        print("Available methods:")
        print(
            "1. __init__(team_id, project_id): Initializes an EndPoints instance with the specified team and "
            "project IDs.")
        print("2. create(name, sku_id, prefix, replica, model_id): Creates an endpoint with the provided details.")
        print("3. get(endpoint_id): Retrieves information about a specific endpoint using its ID.")
        print("4. list(): Lists all endpoints associated with the team and project.")
        print("5. delete(endpoint_id): Deletes an endpoint with the given ID.")
        print("6. clear_values(): Resets the team and project IDs to None.")
        print("7. validate(): Checks if the team and project IDs are of integer type.")
        print("8. help(): Displays this help message.")

        # Example usages
        print("\nExample usages:")
        print("endpoints = EndPoints(123, 456)")
        print("endpoints.create('Name', sku_id, 'Prefix', replica, model_id)")
        print("endpoints.get(789)")
        print("endpoints.list()")
        print("endpoints.delete(789)")
