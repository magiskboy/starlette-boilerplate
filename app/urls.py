from typing import List
from starlette.routing import (
    Route,
    Mount,
)
from starlette.staticfiles import StaticFiles
from . import views
from . import settings


static = StaticFiles(directory=str(settings.STATIC_DIR))

routes: List[Route] = [
    Route('/', views.homepage, name='home'),
    Mount('/static', static, name='static'),
]
