from e2enetworks.cloud.aiplatform import config


class init:
    def __init__(self, access_token, apikey):
        config.apikey = apikey
        config.access_token = access_token

