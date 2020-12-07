from starlette.applications import Starlette
from .urls import routes
from .middlewares import middlewares
from . import settings


def create_app() -> Starlette:
    app = Starlette(
        routes=routes,
        middleware=middlewares,

        debug=settings.DEBUG,
    )

    return app
