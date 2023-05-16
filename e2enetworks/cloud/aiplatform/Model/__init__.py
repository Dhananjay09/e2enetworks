class Model:
    def __init__(self, team, project, credentials=None):
        self.team = team
        self.project = project
        self.credentials = credentials

    def create(self, name=None, bucket_type=None, bucket_name=None, model_type=None):
        pass

    def get(self, model_id):
        pass

    def list(self):
        pass

    def delete(self, model_id):
        pass
