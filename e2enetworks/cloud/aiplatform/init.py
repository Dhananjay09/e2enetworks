import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import (BASE_GPU_URL, STATUS_CODE,
                                                    VALIDATED_SUCCESSFULLY, INVALID_CREDENTIALS)


class init:
    def __init__(self, auth_token, apikey):
        config.apikey = apikey
        config.auth_token = auth_token
        self.validate(auth_token, apikey)

    def validate(self, auth_token, apikey):
        url = f"{BASE_GPU_URL}customer/details/?apikey={apikey}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {auth_token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == STATUS_CODE:
            print(VALIDATED_SUCCESSFULLY)
        else:
            print(INVALID_CREDENTIALS)
            self.clear_values()

    def clear_values(self):
        config.apikey = None
        config.auth_token = None

    @staticmethod
    def help():
        print("Init Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities for initialization.")
        print("\t\tAvailable methods:")
        print("\t\t1. __init__(auth_token, apikey): Initializes an Init instance with the provided authentication"
              " token and API key.")
        print("\t\t2. validate(auth_token, apikey): Validates the provided authentication token and API key.")
        print("\t\t3. clear_values(): Resets the API key and authentication token to None.")
        print("\t\t4. help(): Displays this help message.")

        # Example usage
        print("\t\t\nExample usage:")
        print("\t\tinit = init('Auth Token', 'API Key')")
