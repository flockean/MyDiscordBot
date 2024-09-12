from discord.ext import commands

from src.controller.util_service import Category
from src.database import database_utils
from src.database.database_utils import *
from src.models.schemas import GameProgress, GameType


class GameMmgt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(usage=Category.management)
    async def get_games(self, ctx):
        database_utils.get_all(GameProgress)
        await ctx.send("lul")

    @commands.command(usage=Category.management)
    async def get_category(self, ctx):
        database_utils.get_all(GameType)
        await ctx.send("lol")

async def setup(client):
    await client.add_cog(GameMmgt(client))

