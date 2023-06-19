import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Teams:
    @validate_access_key_and_token
    def create(self, team_name):
        payload = json.dumps({
            "team_name": team_name,
        })
        url = f"{BASE_GPU_URL}teams/?apikey={config.apikey}"

        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("POST", url, headers=headers, data=payload)

    @validate_access_key_and_token
    def get(self, team_id):

        if type(team_id) != int:
            print(f"Team ID - {team_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{team_id}/?apikey={config.apikey}"

        payload = ""

        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("GET", url, headers=headers, data=payload)

    @validate_access_key_and_token
    def list(self):
        url = f"{BASE_GPU_URL}teams/?apikey={config.apikey}"
        payload = ""

        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("GET", url, headers=headers, data=payload)

    @validate_access_key_and_token
    def delete(self, team_id):

        if type(team_id) != int:
            print(f"Team ID - {team_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{team_id}/?apikey={config.apikey}"
        payload = ""

        headers['Authorization'] = f'Bearer {config.auth_token}'
        return requests.request("DELETE", url, headers=headers, data=payload)

    @staticmethod
    def help():
        print("Teams Class Help")
        print("\t\t================")
        print("\t\tThis class provides functionalities to interact with teams.")
        print("\t\tAvailable methods:")
        print("\t\t1. create(team_name): Creates a new team with the provided team name.")
        print("\t\t2. get(team_id): Retrieves information about a specific team using its ID.")
        print("\t\t3. list(): Lists all teams.")
        print("\t\t4. delete(team_id): Deletes a team with the given ID.")
        print("\t\t5. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tteams = Teams()")
        print("\t\tteams.create('Team Name')")
        print("\t\tteams.get(123)")
        print("\t\tteams.list()")
        print("\t\tteams.delete(123)")
