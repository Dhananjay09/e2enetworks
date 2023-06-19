import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


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
        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("POST", url, headers=headers, data=payload)

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
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        
        return response

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/" \
              f"?apikey={config.apikey}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        
        return response

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
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("DELETE", url, headers=headers, data=payload)
        
        return response

    @validate_access_key_and_token
    def logs(self, endpoint_id):

        status, response = self.validate()

        if not status:
            return response

        if type(endpoint_id) != int:
            print(f"EndPoint ID - {endpoint_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/inference/{endpoint_id}/logs/?" \
              f"apikey={config.apikey}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def help():
        print("EndPoint Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities to interact with EndPoint.")
        print("\t\tAvailable methods:")
        print("\t\t1. __init__(team_id, project_id): Initializes an EndPoints instance with the specified team and "
              "project IDs.")
        print("\t\t2. create(name, sku_id, prefix, replica, model_id): Creates an endpoint with the provided details.")
        print("\t\t3. get(endpoint_id): Retrieves information about a specific endpoint using its ID.")
        print("\t\t4. list(): Lists all endpoints associated with the team and project.")
        print("\t\t5. delete(endpoint_id): Deletes an endpoint with the given ID.")
        print("\t\t6. clear_values(): Resets the team and project IDs to None.")
        print("\t\t7. validate(): Checks if the team and project IDs are of integer type.")
        print("\t\t8. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tendpoints = EndPoints(123, 456)")
        print("\t\tendpoints.create('Name', sku_id, 'Prefix', replica, model_id)")
        print("\t\tendpoints.get(789)")
        print("\t\tendpoints.list()")
        print("\t\tendpoints.delete(789)")
