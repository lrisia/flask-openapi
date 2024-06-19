# Flask OpenAPI

Simple Flask API with OpenAPI documentation.

Flask API template with [flask-openapi3](https://github.com/luolingchun/flask-openapi3) documentation. Easy to use and extend.

## Installation

### Virtual Environment

Install by creating a virtual environment with `python3 -m venv .venv`. Then, activating it by

Windows:

```bat
.venv\Scripts\activate
```

Linux/MacOS:

```bash
source .venv/bin/activate
```

### Dotenv

Create a `.env` file by copy from `.env.example` and fill in the values.

```bash
cp .env.example .env
```

- `ENVIROMENT` - Environment of the application. `production` for production mode other value will be development mode.

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage
### Start application
Start appllication have 2 options:

1. Use `python src/index.py` command to launch application. However, this option is **not recommended** for production.
1. Use `flask` command or anything else to launch application. To use this option, you need to change directory to `src` folder first, with command `cd src`. Then, use `flask run` to launch application.

for option 2, you can see more detail in [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/deploying/)

### OpenAPI Documentation
By default, OpenAPI documentation is available at `/api/docs` endpoint.

### Implementation
- [src/index.py](src/index.py) - Main application entrypoint.
- [src/api/register_routes.py](src/api/register_routes.py) - Add routes here.
- [src/api/schema.py](src/api/schema.py) - Define tag, common request/response schema or anything eles here.
- [src/api/controller](src/api/controllers/) - Create any route class in this folder

For instance, create [`echo_post.py`](src/api/controllers/echo/echo_post.py) as a new route by creating a new file in `src/api/controllers/echo` folder. Then, after finish your code in new route, don't forget to adding new route to [`src/api/register_routes.py`](src/api/register_routes.py) for register route. Otherwise, route wouldn't reached.

### Simple route example
```python
from http import HTTPStatus

from api.routes import Api
from api.schema import ApiTag, DefaultErrorResponse
from api.schema.example import ExampleResponse

class ExampleRoute(Api):
    def register(self, app):
        @app.get(
            "/example",
            description="Example route",
            tags=[ApiTag.Example],
            responses={
                HTTPStatus.OK: ExampleResponse,
                HTTPStatus.INTERNAL_SERVER_ERROR: DefaultErrorResponse,
            },
        )
        def example():
            try:
                return ExampleResponse(message="example").model_dump(), HTTPStatus.OK
            except Exception as e:
                return (
                    DefaultErrorResponse(stacktrace=e.__str__()).model_dump(),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )
```

