import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL, BUCKET_TYPES, MODEL_TYPES
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


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
        return True, "Success"

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
        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("POST", url, headers=headers, data=payload)

    @validate_access_key_and_token
    def get(self, model_id):

        status, response = self.validate()

        if not status:
            return response

        if type(model_id) != int:
            print(f"Model ID - {model_id} Should be Integer")
            return

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/{model_id}" \
              f"?apikey={config.apikey}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("GET", url, headers=headers, data=payload)

    @validate_access_key_and_token
    def list(self):

        status, response = self.validate()

        if not status:
            return response

        url = f"{BASE_GPU_URL}teams/{self.team_id}/projects/{self.project_id}/serving/model/" \
              f"?apikey={config.apikey}"

        payload = ""
        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        
        return response

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
        headers['Authorization'] = f'Bearer {config.auth_token}'

        return requests.request("DELETE", url, headers=headers, data=payload)

    @staticmethod
    def help():
        print("Models Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities to interact with models.")
        print("\t\tAvailable methods:")
        print(
            "\t\t1. __init__(team_id, project_id): Initializes a Models instance with the specified team and project "
            "IDs.")
        print("\t\t2. create(name, bucket_type, bucket_name, model_type): Creates a new model with the provided "
              "details.")
        print("\t\t3. get(model_id): Retrieves information about a specific model using its ID.")
        print("\t\t4. list(): Lists all models associated with the team and project.")
        print("\t\t5. delete(model_id): Deletes a model with the given ID.")
        print("\t\t6. clear_values(): Resets the team and project IDs to None.")
        print("\t\t7. validate(): Checks if the team and project IDs are of integer type.")
        print("\t\t8. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tmodels = Models(123, 456)")
        print(f"\t\tmodels.create(name='Test Dataset', bucket_name='dataset-bucket', bucket_type={BUCKET_TYPES},"
              f" model_type={MODEL_TYPES})")
        print("\t\tmodels.get(789)")
        print("\t\tmodels.list()")
        print("\t\tmodels.delete(789)")
