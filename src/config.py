import os
from enum import Enum
from dotenv import load_dotenv


class Environment(Enum):
    development = "development"
    production = "production"


class _Config:
    SRC_DIR: str = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR: str = os.path.join(SRC_DIR, "..")
    """
    Define .env variables here.
    """

    ENVIRONMENT: str

    def __init__(self):
        load_dotenv()
        """
        Get and define default value for environment variable here.
        """
        self.ENVIRONMENT = os.environ.get("ENVIRONMENT", Environment.development.value)


config = _Config()


def Config() -> _Config:
    return config
