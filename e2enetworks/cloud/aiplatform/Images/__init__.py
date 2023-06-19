import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Images:

    @validate_access_key_and_token
    def list(self):
        url = f"{BASE_GPU_URL}gpu_service/image/?apikey={config.apikey}"
        payload = ""

        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    @staticmethod
    def help():
        print("Images Class Help")
        print("\t\t================")
        print("\t\tThis class provides functionalities to interact with Images.")
        print("\t\tAvailable methods:")

        print("\t\t1. list(): Lists all Images.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\timages = Images()")
        print("\t\timages.list()")
