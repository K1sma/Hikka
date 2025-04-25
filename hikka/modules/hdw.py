from telethon.sessions import StringSession
from .. import loader
import os

@loader.tds
class AutologinMod(loader.Module):
    """Автовход по строке сессии"""
    strings = {"name": "Autologin"}

    async def client_ready(self, client, db):
        if not client.is_connected():
            await client.start(
                session=StringSession(os.getenv("SESSION_STRING")),
                api_id=int(os.getenv("API_ID")),
                api_hash=os.getenv("API_HASH")
            )
        await client.send_message("me", "🔒 Автовход выполнен!")
