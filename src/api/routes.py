from abc import ABC, abstractmethod
from flask_openapi3 import APIBlueprint


class Api(ABC):

    @abstractmethod
    def register(self, app: APIBlueprint):
        pass


class RouteList:
    api_blueprint: APIBlueprint

    def __init__(self, blueprint: APIBlueprint) -> None:
        self.api_blueprint = blueprint

    def add(self, route: Api):
        route.register(self.api_blueprint)
