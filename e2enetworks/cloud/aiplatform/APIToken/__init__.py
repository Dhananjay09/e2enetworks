import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class APITokens:
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
    def create(self, auth_token):

        status, response = self.validate()

        if not status:
            return response

        payload = json.dumps({
            "auth_token": auth_token,
        })

        headers['Authorization'] = f'Bearer {config.auth_token}'

        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/?apikey={config.apikey}&project_id={self.project_id}"

        response = requests.request("POST", url, headers=headers, data=payload)

        

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/?apikey={config.apikey}&project_id={self.project_id}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        

    @validate_access_key_and_token
    def delete(self, token_id):

        status, response = self.validate()

        if not status:
            return response

        if type(token_id) != int:
            print(f"Token ID - {token_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/auth-token/{token_id}/?apikey={config.apikey}&project_id=" \
              f"{self.project_id}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response

    @staticmethod
    def help():
        print("APITokens Class Help")
        print("\t\t====================")
        print("\t\tThis class provides functionalities to manage API tokens.")
        print("\t\tAvailable methods:")
        print(
            "\t\t1. __init__(team_id, project_id): Initializes an APITokens instance with the specified team ID and "
            "project ID.")
        print("\t\t2. create(auth_token): Creates a new API token with the provided authentication token.")
        print("\t\t3. list(): Lists all API tokens associated with the team and project.")
        print("\t\t4. delete(token_id): Deletes an API token with the given token ID.")
        print("\t\t5. clear_values(): Resets the team ID and project ID to None.")
        print("\t\t6. validate(): Checks if the team ID and project ID are of integer type.")
        print("\t\t7. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tapi_tokens = APITokens(123, 456)")
        print("\t\tapi_tokens.create('auth_token')")
        print("\t\tapi_tokens.list()")
        print("\t\tapi_tokens.delete(789)")