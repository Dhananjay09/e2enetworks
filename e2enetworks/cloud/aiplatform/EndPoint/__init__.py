class EndPoint:
    def __init__(self, model=None, sku_id=None, storage_url=None, replica=None):
        self.model = model
        self.sku_id = sku_id,
        self.storage_url = storage_url,
        self.replica = replica

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
