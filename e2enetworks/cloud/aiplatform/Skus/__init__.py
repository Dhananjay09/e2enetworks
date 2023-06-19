import requests

from e2enetworks.cloud.aiplatform import config
from e2enetworks.cloud.aiplatform.constants import BASE_GPU_URL
from e2enetworks.cloud.aiplatform.decorators.validate_access_key_and_token import validate_access_key_and_token
from e2enetworks.cloud.aiplatform.constants import headers


class Skus:

    @validate_access_key_and_token
    def list(self, image_id, service):

        if type(image_id) != int:
            print(f"Image ID - {image_id} Should be Integer")
            return

        if type(service) != str:
            print(f"Service - {service} Should be String")
            return

        url = f"{BASE_GPU_URL}gpu_service/sku/?apikey={config.apikey}&image_id={image_id}&service={service}"
        payload = ""

        headers['Authorization'] = f'Bearer {config.auth_token}'

        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    @staticmethod
    def help():
        print("Sku Class Help")
        print("\t\t================")
        print("\t\tThis class provides functionalities to interact with Skus.")
        print("\t\tAvailable methods:")

        print("\t\t1. list(image_id, service): Lists all Skus for given image_id and service.")
        print("\t\t Allowed Services List - ['notebook', 'inference']")
        # Example usages
        print("\t\tExample usages:")
        print("\t\tskus = Skus()")
        print("\t\tskus.list(image_id, service)")
