class Model:
    def __init__(self, name=None, type=None, bucket_name=None, model_type=None, init=None):
        self.name = name
        self.type = type
        self.bucket_name = bucket_name
        self.model_type = model_type
        self.credentials = init

    @classmethod
    def create(cls):
        pass

    @classmethod
    def get(cls, model_name):
        pass

    @classmethod
    def list(cls):
        pass

    @classmethod
    def delete(cls):
        pass
