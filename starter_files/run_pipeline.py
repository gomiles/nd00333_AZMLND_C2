import os

from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.pipeline.core import PublishedPipeline
from azureml.core import Workspace
import requests

interactive_auth = InteractiveLoginAuthentication()
auth_header = interactive_auth.get_authentication_header()

subscription_id = os.getenv("SUBSCRIPTIONID")
resource_group = os.getenv("RESOURCEGROUP")
workspace_name = os.getenv("WORKSPACENAME")

ws = Workspace(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name, auth=interactive_auth)

published_pipeline = PublishedPipeline.get(ws, 'f43f5605-9636-4cd3-9f75-7f97053224db')
pipeline_endpoint = published_pipeline.endpoint

response = requests.post(pipeline_endpoint, headers=auth_header, json={"ExperimentName": "udacity-automlstep-classification"})
print(response)
print(response.json())
