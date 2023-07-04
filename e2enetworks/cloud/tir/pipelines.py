import requests 
import json
from typing import Optional, Dict
from e2enetworks.cloud.tir import client, utils

class PipelineClient():
    def __init__(
        self,
        project: Optional[str] = None,
    ):  
        client_not_ready = (
            "Client is not ready. Please initiate client by:"
            "\n- Using e2enetworks.cloud.tir.init(...)"
        )
        if not client.Default.ready():
            raise ValueError(client_not_ready)
        
        if project:
            client.Default.set_project(project)
    
    def list_pipelines(
        self,
        page_token: str = '',
        page_size: int = 10,
        sort_by: str = '',
        filter: Optional[str] = None
    ):  
        url = "{project_path}/pipelines/".format(project_path=client.Default.gpu_projects_path())
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return response

    def create_experiment(
        self,
        name: str,
        description: Optional[str] = None,
    ):
        request_params = {
            'name': name,
            'description': description,
        }
        url = "{project_path}/pipelines/experiments/".format(project_path=client.Default.gpu_projects_path())
        req = requests.Request('POST', url, data=request_params)
        response = client.Default.make_request(req)
        return response

    def list_experiments(
        self,
        page_token: str = '',
        page_size: int = 10,
        sort_by: str = '',
        filter: Optional[str] = None
    ):
        url = "{project_path}/pipelines/experiments/".format(project_path=client.Default.gpu_projects_path())
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return response

    