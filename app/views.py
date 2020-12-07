from starlette.requests import Request
from starlette.templating import Jinja2Templates
from . import settings

templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))


def homepage(request: Request):
    template = 'homepage.html'
    context = {'request': request}

    return templates.TemplateResponse(template, context)
