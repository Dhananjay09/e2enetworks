from e2enetworks.cloud.aiplatform import config
MY_ACCOUNT_LB_URL = "https://api.e2enetworks.com/myaccount/"
GPU_URL = "api/v1/gpu/"
BASE_GPU_URL = f"{MY_ACCOUNT_LB_URL}{GPU_URL}"
INDENTATION = 4
STATUS_CODE = 200
VALIDATED_SUCCESSFULLY = "Validated Successfully"
INVALID_CREDENTIALS = "Validated Failed Invalid APIkey of Toekn"
headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://gpu-notebooks.e2enetworks.com',
            'Referer': 'https://gpu-notebooks.e2enetworks.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
MANAGED_STORAGE = "managed"
E2E_OBJECT_STORAGE = "e2e_s3"
BUCKET_TYPES = [MANAGED_STORAGE, E2E_OBJECT_STORAGE]
BUCKET_TYPES_HELP = {
    MANAGED_STORAGE: "To Create New Bucket",
    E2E_OBJECT_STORAGE: " To Use Existing Bucket"
}

