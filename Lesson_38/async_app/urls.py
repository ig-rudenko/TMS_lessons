from aiohttp import web

from . import views

routes = [
    web.get("/", views.HomeView),  # Только метод get!
]
