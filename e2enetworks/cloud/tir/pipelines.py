from typing import Optional, Dict
from e2enetworks.cloud.tir import initializer, utils
from  kfp_server_api import ApiListPipelinesResponse

class PipelineClient():
    def __init__(
        self,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None, 
        project: Optional[str] = None,
        team: Optional[str] = None,
    ):  
        self.pipeline_client = initializer.default_config.create_pipeline_client(access_token=access_token, project=project, team=team)
        
        self.namespace = initializer.default_config.namespace(project)
    
    def list_pipelines(
        self,
        page_token: str = '',
        page_size: int = 10,
        sort_by: str = '',
        filter: Optional[str] = None
    ) -> ApiListPipelinesResponse:
        return self.pipeline_client.list_pipelines(page_token, page_size, sort_by, filter)
