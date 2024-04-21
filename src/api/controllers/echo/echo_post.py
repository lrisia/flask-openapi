from http import HTTPStatus
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from api.routes import Api
from api.schema import ApiTag, DefaultErrorResponse


class EchoPostRequest(BaseModel):
    body: Dict[str, Any] = Field(description="This body will be echoed back.")


class EchoPostQuery(BaseModel):
    time: Optional[int] = Field(description="Amount of body will be echoed back.")


class EchoPostResponse(BaseModel):
    body: Dict[str, Any] = Field(description="This body will be echoed back.")


class EchoPostResponseList(BaseModel):
    body: List[EchoPostResponse] = Field(description="This body will be echoed back.")


class EchoPostRoute(Api):
    def register(self, app):
        @app.post(
            "/echo",
            description="Echo the request body back.",
            tags=[ApiTag.Echo],
            responses={
                HTTPStatus.OK: EchoPostResponseList,
                HTTPStatus.INTERNAL_SERVER_ERROR: DefaultErrorResponse,
            },
        )
        def echo(body: EchoPostRequest, query: EchoPostQuery):
            try:
                time = 1 if query.time is None else query.time
                return [
                    EchoPostResponse(body=body.body).model_dump() for i in range(time)
                ], HTTPStatus.OK
            except Exception as e:
                return (
                    DefaultErrorResponse(stacktrace=e.__str__()).model_dump(),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )
