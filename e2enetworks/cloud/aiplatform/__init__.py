import json
from e2enetworks.cloud.aiplatform.init import init
from e2enetworks.cloud.aiplatform.Images import Images
from e2enetworks.cloud.aiplatform.Skus import Skus
from e2enetworks.cloud.aiplatform.Notebooks import Notebooks
from e2enetworks.cloud.aiplatform.Dataset import Datasets
from e2enetworks.cloud.aiplatform.EndPoint import EndPoints
from e2enetworks.cloud.aiplatform.Model import Models
from e2enetworks.cloud.aiplatform.Project import Projects
from e2enetworks.cloud.aiplatform.Teams import Teams
from e2enetworks.cloud.aiplatform.APIToken import APITokens


def help():
    print("\t\tAIPlatform Help")
    print("\t\t=================")
    print("\t\tAvailable classes:")
    print("\t\t- init: Provides functionalities for initialization.")
    print("\t\t- Images: Provides functionalities to interact with images.")
    print("\t\t- Skus: Provides functionalities to interact with skus.")
    print("\t\t- Notebooks: Provides functionalities to interact with notebooks.")
    print("\t\t- Datasets: Provides functionalities to interact with datasets.")
    print("\t\t- EndPoints: Provides functionalities to interact with endpoints.")
    print("\t\t- Models: Provides functionalities to interact with models.")
    print("\t\t- Projects: Provides functionalities to interact with projects.")
    print("\t\t- Teams: Provides functionalities to interact with teams.")
    print("\t\t- APITokens: Provides functionalities to interact with API tokens.")
    print("\t\t- beautify: beautify and print the specific response")

    # Call help() method on each class
    init.help()
    Images.help()
    Skus.help()
    Notebooks.help()
    Datasets.help()
    EndPoints.help()
    Models.help()
    Projects.help()
    Teams.help()
    APITokens.help()


def beautify(response):
    print(json.dumps(response.json(), indent=5))
