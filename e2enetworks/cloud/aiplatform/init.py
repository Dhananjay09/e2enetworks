class init:
    def __init__(self, access_key, api_token):
        self.access_key = access_key
        self.api_token = api_token

    @classmethod
    def api_token(cls):
        return cls.api_token

    @classmethod
    def access_key(cls):
        return cls.access_key
