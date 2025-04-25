from .. import loader
from aiohttp import web
import os

@loader.tds
class KeepAliveMod(loader.Module):
    """Поддержка 24/7 работы на Render"""
    strings = {"name": "KeepAlive"}

    async def client_ready(self, client, db):
        app = web.Application()
        app.router.add_get("/ping", lambda r: web.Response(text="OK"))
        runner = web.AppRunner(app)
        await runner.setup()
        await web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 8080))).start()
