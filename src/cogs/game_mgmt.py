from discord.ext import commands

from src.controller.util_service import Category, fancy_enumeration, fancy_enumeration_categorys
from src.database import database_utils
from src.database.database_utils import *
from src.models.schemas import GameProgress, GameType, ProgressStatus
import re
import logging

class GameMmgt(commands.Cog):

    input_single = r'(\w+)'
    input_full = r'"(\w+:\w+")'
    input_full_game = r'(\w+:)'

    def __init__(self, client):
        self.client = client

    # TODO: does not work at please fix
    @commands.command(usage=Category.management)
    async def get_games(self, ctx):
        logging.info("getgames has been triggerd")
        games = database_utils.get_all(GameProgress)
        logging.info(games)
        await ctx.send(games)

    @commands.command(usage=Category.management)
    async def get_category(self, ctx):
        await ctx.send(
            fancy_enumeration(database_utils.get_all(GameType)))

    @commands.command(usage=Category.management)
    async def set_category(self, ctx, *, args):
        logging.info(args)
        matches = re.findall(self.input_single, args)
        if matches:
            logging.info(matches)
            for match in matches:
                database_utils.add(
                    GameType(id_name=match)
                )
        await ctx.send("Category has been added")

    # TODO: does not work yet
    @commands.command(usage=Category.management)
    async def set_game(self, ctx, *, args):
        matches = re.findall(self.input_single, args)
        if matches:
            logging.info(matches)
            for match in matches:
                database_utils.add(
                GameProgress(id_name=match,
                             game_type="Hamburger",
                             in_progress=ProgressStatus.notStarted)
                )
        await ctx.send("Game has been added")


async def setup(client):
    await client.add_cog(GameMmgt(client))

