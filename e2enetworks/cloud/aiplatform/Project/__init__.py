import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, INDENTATION
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Projects:
    def __init__(self, team_id):
        self.team_id = team_id
        self.validate()

    def validate(self):
        if type(self.team_id) != int:
            print(f"Team Id -{self.team_id} Should be Integer")
            return False, f"Team Id -{self.team_id}should be Integer"
        return True, "Success"

    def clear_values(self):
        self.team_id = None

    @validate_access_key_and_token
    def create(self, project_name):

        status, response = self.validate()

        if not status:
            return response

        payload = json.dumps({
            "project_name": project_name,
        })

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("POST", url, headers=headers, data=payload)

        
        return response

    @validate_access_key_and_token
    def get(self, project_id):

        status, response = self.validate()

        if not status:
            return response

        if type(project_id) != int:
            print(f"Project ID - {project_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        
        return response

    @validate_access_key_and_token
    def list(self):
        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/?apikey={config.apikey}"
        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        
        return response

    @validate_access_key_and_token
    def delete(self, project_id):

        status, response = self.validate()

        if not status:
            return response

        if type(project_id) != int:
            print(f"Project ID - {project_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{project_id}/?apikey={config.apikey}"
        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("DELETE", url, headers=headers, data=payload)
        
        return response

    @staticmethod
    def help():
        print("Projects Class Help")
        print("\t\t===================")
        print("\t\tThis class provides functionalities to interact with projects.")
        print("\t\tAvailable methods:")
        print("\t\t1. __init__(team_id): Initializes a Projects instance with the specified team ID.")
        print("\t\t2. create(project_name): Creates a new project with the provided project name.")
        print("\t\t3. get(project_id): Retrieves information about a specific project using its ID.")
        print("\t\t4. list(): Lists all projects associated with the team.")
        print("\t\t5. delete(project_id): Deletes a project with the given ID.")
        print("\t\t6. clear_values(): Resets the team ID to None.")
        print("\t\t7. validate(): Checks if the team ID is of integer type.")
        print("\t\t8. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tprojects = Projects(123)")
        print("\t\tprojects.create('Project Name')")
        print("\t\tprojects.get(456)")
        print("\t\tprojects.list()")
        print("\t\tprojects.delete(456)")
