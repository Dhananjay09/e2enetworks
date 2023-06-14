from e2enetworks.cloud.aiplatform.Dataset import Datasets
from e2enetworks.cloud.aiplatform.EndPoint import EndPoints
from e2enetworks.cloud.aiplatform.init import init
from e2enetworks.cloud.aiplatform.Model import Models
from e2enetworks.cloud.aiplatform.Project import Projects
from e2enetworks.cloud.aiplatform.Teams import Teams
from e2enetworks.cloud.aiplatform.APIToken import APITokens


def help():
    print("AIPlatform Help")
    print("=================")
    print("Available classes:")
    print("- Datasets: Provides functionalities to interact with datasets.")
    print("- EndPoints: Provides functionalities to interact with endpoints.")
    print("- Init: Provides functionalities for initialization.")
    print("- Models: Provides functionalities to interact with models.")
    print("- Projects: Provides functionalities to interact with projects.")
    print("- Teams: Provides functionalities to interact with teams.")
    print("- APITokens: Provides functionalities to interact with API tokens.")

    # Call help() method on each class
    Datasets(team_id=1, project_id=2).help()
    EndPoints(team_id=1, project_id=2).help()
    init(auth_token="", apikey="").help()
    Models(team_id=1, project_id=2).help()
    Projects(team_id=1).help()
    Teams().help()
    APITokens(team_id=1, project_id=2).help()
