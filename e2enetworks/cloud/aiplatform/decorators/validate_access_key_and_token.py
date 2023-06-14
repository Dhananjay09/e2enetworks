from e2enetworks.cloud.aiplatform import config


def validate_access_key_and_token(func):
    def inner1(*args, **kwargs):
        if not config.apikey:
            return f"APIKEY = {config.apikey} is not Valid"
        if not config.auth_token:
            return f"AUTH-TOKEN = {config.auth_token} is not Valid"
        func(*args, **kwargs)
    return inner1
