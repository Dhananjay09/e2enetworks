from e2enetworks.cloud.tir import version as tir_version

__version__ = tir_version.__version__
from e2enetworks.cloud.tir import client
from e2enetworks.cloud.tir.pipelines import PipelineClient
init = client.Default.init

__all__ = (
    "init",
    "PipelineClient"
)