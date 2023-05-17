from e2enetworks.cloud.aiplatform import config


class init:
    def __init__(self, access_key, api_token):
        config.access_key = access_key
        config.api_token = api_token

