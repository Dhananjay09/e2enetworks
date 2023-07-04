import os
import kfp
from e2enetworks.cloud.tir import client
from typing import Optional
from requests import Request, Session, Response
import e2enetworks.constants as constants

E2E_UI_HOST = "localhost:3000"

class _Client:
    def __init__(self):
        self._api_key = None
        self._access_token = None
        self._project = None
        self._team = None
        self._namespace = None
        self._eos_bucket = None
        self._api_host = None
        self._client = None

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
        self._api_key = api_key
        self._project = project
        self._team = team
        self._eos_bucket = eos_bucket

    def ready(self): 
        return False if not self.api_key() or not self.access_token() else True
    
    def api_host(self):
        if self._api_host:
            return self._api_host
        if os.environ.get("E2E_TIR_API_HOST"):
            self._api_host = os.environ.get("E2E_TIR_API_HOST")
            return self._api_host
        return constants.MY_ACCOUNT_LB_URL
    
    def access_token(self):
        if self._access_token:
            return self._access_token

        access_token_not_set = (
            "Access Token not set. Please provide a Access Token by:"
            "\n- Using e2enetworks.cloud.tir.init(access_token=)"
            "\n- Setting an environment variable E2E_TIR_ACCESS_TOKEN"
        )

        if os.environ.get("E2E_TIR_ACCESS_TOKEN"):
            self._access_token = os.environ.get("E2E_TIR_ACCESS_TOKEN")
            return self._access_token
        else:
            raise ValueError(access_token_not_set)

    def api_key(self):
        if self._api_key:
            return self._api_key

        api_key_not_set = (
            "API key not set. Please provide api key by:"
            "\n- Using e2enetworks.cloud.tir.init(api_key=)"
            "\n- Setting an environment variable E2E_TIR_API_KEY"
        )

        if os.environ.get("E2E_TIR_API_KEY"):
            self._api_key = os.environ.get("E2E_TIR_API_KEY")
            return self._api_key
        else:
            raise ValueError(api_key_not_set)

    def set_project(self, project):
        self._project = project

    def gpu_projects_path(self, project=None):
        if not project:
            project=  self.project()
        
        return "{api_host}/api/v1/gpu/projects/{project}".format(api_host=self.api_host(), project=project)
    
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
    
    def make_request(self, request, stream=None, verify=None, timeout=None) -> Response:
        '''
            make_request(self, request): is common method to prepare a request
            and send to API host. 
            
            input:
            - request: requests.request. the request url must be only the path and 
            should not contain api host. 
            example usage: 
                request = requests.Request("GET", "http://localhost/api/v1/pipelines")
                make_request(request)

            output:
            - http response
            
            The modifications made to the request will be:
            * include auth header and add api key query param
            * append api host to the path 
        '''    
        s = Session()
        prepped = s.prepare_request(request)

        # append api key. we expect caller to send & if query parameters are used.
        # for example:
        #   if the request url has query parameters like below
        #       /pipelines?page=2 
        #   then we expect the caller to set url as /pipelines?page=2& instead of /pipelines?page=2
        # 
        prepped.url = f"{prepped.url}?" if prepped.url[len(prepped.url)-1] == "/" else prepped.url
        prepped.url = "{}api_key={}".format(prepped.url, self.api_key()) 
        print("prepped.url:", prepped.url)
        prepped.headers["Authorization"] = f"Bearer {self.access_token()}"

        return s.send(prepped, stream=stream, verify=verify, timeout=timeout)

# common client set by tir.init(access_token=..., api_key=...)
Default = _Client()
