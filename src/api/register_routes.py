from api.controllers.echo.echo_post import EchoPostRoute
from api.controllers.healthcheck import HealthCheck

"""
Add API route here.
"""
routes = [
    HealthCheck(),
    EchoPostRoute()
]
