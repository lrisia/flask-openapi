from typing import Annotated, Any, Optional
from flask_openapi3 import Tag
from pydantic import BaseModel, BeforeValidator


class ApiTag:
    """
    Add API tag here.
    """

    Utils = Tag(name="Util", description="Utility functions")
    Echo = Tag(name="Echo", description="Example echo route")

class DefaultErrorResponse(BaseModel):
    stacktrace: Optional[Any]
