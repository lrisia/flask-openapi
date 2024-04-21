from http import HTTPStatus

from pydantic import BaseModel, Field
from api.schema import ApiTag
from api.routes import Api


class HealthCheckResponse(BaseModel):
    status: str = Field(description="Healthcheck status")


class HealthCheck(Api):
    def register(self, app):
        @app.get(
            "/healthcheck",
            description="Healthcheck",
            tags=[ApiTag.Utils],
            responses={HTTPStatus.OK: HealthCheckResponse},
        )
        def healthcheck():
            return HealthCheckResponse(status="ok").model_dump(), HTTPStatus.OK
