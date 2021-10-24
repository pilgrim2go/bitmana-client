import simplejson as json

from .core import (
    ApiClient,
    BaseClient,
    who_am_i,
    JelasticClientException
)
from .env_info import EnvInfo
from .env_settings import EnvSettings
from .env_status import EnvStatus
from .node_settings import MultipleNodeSettings


class DeployClient(BaseClient):
    jelastic_group = "environment"

    jelastic_class = "deployment"

    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def deploy_archive(self, env_name, file_url, file_name):
        response = self._execute(who_am_i(), envName =env_name, fileUrl =file_url,fileName=file_name)
        return response
