from flask_openapi3 import Info
from flask_openapi3 import OpenAPI, APIBlueprint, Tag, Info

from config import Config, Environment
from api.routes import RouteList
from api.register_routes import routes


class Server:
    __app: OpenAPI
    __api_prefix: str

    def __init__(self, api_prefix: str = "/api"):
        self.__api_prefix = api_prefix
        self.__app = OpenAPI(
            __name__,
            info=Info(title="Flask OpenAPI", version="1.0.0"),
            doc_prefix=f"{api_prefix}/docs",
            swagger_url="/",
        )
        self.__register_routes()

    def __register_routes(self):
        route_list = RouteList(
            APIBlueprint("api", __name__, url_prefix=self.__api_prefix)
        )
        for route in routes:
            route_list.add(route)
        self.__app.register_api(route_list.api_blueprint)

    def run(
        self, ip: str | None = None, port: int | None = None, debug: bool | None = None
    ):
        if ip is None:
            ip = (
                "0.0.0.0"
                if Config().ENVIRONMENT == Environment.production.value
                else None
            )
        if debug is None:
            debug = (
                False if Config().ENVIRONMENT == Environment.production.value else True
            )
        self.__app.run(host=ip, port=port, debug=debug)
        
    def get_app(self):
        return self.__app
