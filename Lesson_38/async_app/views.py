from aiohttp import web
from aiohttp_jinja2 import template

from .models import Post


class HomeView(web.View):
    @template("home.html")
    async def get(self):
        all_posts = await Post.all()
        print(all_posts)
        print(all_posts[0])
        # Возвращаем контекст в шаблон.
        return {"title": "Hello World", "user": "Anonymous", "posts": all_posts}
