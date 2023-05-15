class Dataset:
    def __init__(self, bucket_name=None, type=None, credentials=None):
        self.bucket_name = bucket_name
        self.type = type

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
