# Post random bible verse

# Discord
import discord
# Red
from redbot.core import commands
# Libs
import aiohttp


class Bible(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def cog_unload(self):
        await self.session.close()

    @commands.command()
    async def bible(self, ctx):
        
        url = "https://bible-api.com/?random=verse"
        async with self.session.get(url) as r:
            json_body = await r.json()
            verse_info = json_body['verses'][0]
            await ctx.send(f"\"*{verse_info['text'].rstrip()}*\" ~ {verse_info['book_name']} {verse_info['chapter']}:{verse_info['verse']}")

