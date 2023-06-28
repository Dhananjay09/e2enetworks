import os
import kfp
from e2enetworks.cloud.tir import initializer
from typing import Optional

E2E_UI_HOST = "localhost:3000"

class Config:
    def __init__(self):
        self._apikey = None
        self._access_token = None
        self._project = None
        self._team = None
        self._namespace = None
        self._eos_bucket = None
        self._kfp_host = None
        self._pipeline_client = None

    def init(
        self,
        *,
        api_key: Optional[str],
        access_token: Optional[str],
        project: Optional[str] = None,
        team: Optional[str] = None,
        eos_bucket: Optional[str] = None,
    ):
        self._access_token = access_token
        self._apikey = api_key
        self._project = project
        self._team = team
        self._eos_bucket = eos_bucket

    def project(self):
        if self._project:
            return self._project
        
        project_not_set = (
            "Project ID not set. Please provide a project ID by:"
            "\n- Using e2enetworks.cloud.tir.init()"
            "\n- Setting an environment variable E2E_TIR_PROJECT_ID"
        )

        if os.environ.get("E2E_TIR_PROJECT_ID"):
            self._project = os.environ.get("E2E_TIR_PROJECT_ID")
            return self._project
        else:
            raise ValueError(project_not_set)

    def namespace(self, project=None):
        if not project:
            project = self.project()

        return  "p-{}".format(project)

    def team(self):
        if self._team:
            return self._team
        
        team_not_set = (
            "Team ID not set. Please provide a team ID by:"
            "\n- Using e2enetworks.cloud.tir.init()"
            "\n- Setting an environment variable E2E_TIR_TEAM_ID"
        )

        if os.environ.get("E2E_TIR_TEAM_ID"):
            self._project = os.environ.get("E2E_TIR_TEAM_ID")
            return self._project
        else:
            raise ValueError(team_not_set)

    def kfp_host(self):
        if self._kfp_host:
            return self._kfp_host
        
        return "http://216.48.188.198"

    def create_pipeline_client(self, access_token=None, project=None, team=None):

        pipeline_host = "{}/{}".format(self.kfp_host(), "pipeline")
        if not access_token:
            access_token = self._access_token
        if not project:
            project = self.project()

        self._pipeline_client = kfp.Client(host=pipeline_host, existing_token=access_token, namespace=self.namespace(), ui_host=E2E_UI_HOST)
        return self._pipeline_client

# common config set by tir.init(access_token=..., api_key=...)
default_config = Config()
