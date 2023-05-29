import json

import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.constants import (BASE_GPU_URL, INDENTATION, STATUS_CODE,
                                   VALIDATED_SUCCESSFULLY)


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
            print(json.dumps(response.json(), indent=INDENTATION))
