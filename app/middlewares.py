from typing import List
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.errors import ServerErrorMiddleware
from starlette.middleware.gzip import GZipMiddleware


middlewares: List[Middleware] = [
    Middleware(CORSMiddleware, allow_origins=['*']),
    Middleware(ServerErrorMiddleware),
    Middleware(GZipMiddleware, minimum_size=1000),
]
