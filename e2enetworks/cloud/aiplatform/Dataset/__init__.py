import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, BUCKET_TYPES, BUCKET_TYPES_HELP
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Datasets:
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

    def create(self, name=None, bucket_name=None, bucket_type=None, description=""):

        if bucket_type not in BUCKET_TYPES:
            print(f"Bucket Type Should be in {BUCKET_TYPES}")
            print(BUCKET_TYPES_HELP)
            return f"Bucket Type Should ne in {BUCKET_TYPES}"

        data = {
            "type": bucket_type,
            "name": name,
            "bucket_name": bucket_name,
            "description": description,
        }
        payload = json.dumps(data)
        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/?apikey={config.apikey}"
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    def get(self, dataset_id):
        status, response = self.validate()

        if not status:
            return response

        if type(dataset_id) != int:
            print(f"Dataset ID - {dataset_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/{dataset_id}/" \
              f"?apikey={config.apikey}"

        headers['Authorization'] = f'Bearer {config.auth_token}'
        payload = ""

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/?apikey={config.apikey}"

        headers['Authorization'] = f'Bearer {config.auth_token}'
        payload = ""

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    def delete(self, dataset_id):
        status, response = self.validate()

        if not status:
            return response

        if type(dataset_id) != int:
            print(f"Dataset ID - {dataset_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/datasets/{dataset_id}/" \
              f"?apikey={config.apikey}"

        headers['Authorization'] = f'Bearer {config.auth_token}'
        payload = ""

        response = requests.request("DELETE", url, headers=headers, data=payload)

        return response

    @staticmethod
    def help():
        print("Datasets Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities to interact with Datasets.")
        print("\t\tAvailable methods:")
        print(
            "\t\t1. __init__(team_id, project_id): Initializes a Datasets instance with the specified team and "
            "project IDs.")
        print(f"\t\t2. create(name, bucket_name=, bucket_type, description): Creates a new dataset with the provided"
              f"name, bucket name, bucket type and description\n Bucket Name is not required in case of"
              f" bucket_type='managed'")
        print("\t\t3. get(bucket_name): Retrieves information about a specific dataset using its bucket name.")
        print("\t\t4. list(): Lists all datasets associated with the team and project.")
        print("\t\t5. delete(bucket_name): Deletes a dataset with the given bucket name.")
        print("\t\t6. clear_values(): Resets the team and project IDs to None.")
        print("\t\t7. validate(): Checks if the team and project IDs are of integer type.")
        print("\t\t8. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tdatasets = Datasets(123, 456)")
        print(f"\t\tdatasets.create(name='Test Dataset', bucket_name='dataset-bucket', bucket_type={BUCKET_TYPES},"
              f" description='Test Dataset')")
        print("\t\tdatasets.get('Bucket Name')")
        print("\t\tdatasets.list()")
        print("\t\tdatasets.delete('Bucket Name')")
