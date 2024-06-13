import datetime
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import os

from src.controller import util_service
from src.database import database_utils
from src.models.schemas import Message, Guild, GuildChannel

# Generate Discord-Bot client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="f!_")
logging.basicConfig(level=logging.INFO)

protocolBool = False



def start_bot():
    load_dotenv()
    # Start the bot
    client.run(os.getenv('DISCORD_BOT'))



@client.event
async def on_ready():
    print(f'Bot ist nun online: {client.user.name}')
    logging.info("BotStats: " + str(client.user) + " Id: " + str(client.application_id))
    for guild in client.guilds:
        database_utils.add(Guild(id=guild.id, name=guild.name))
        for channel in guild.channels:
            database_utils.add(GuildChannel(id=channel.id, name=channel.name, guild_id=guild.id))
    logging.info("Guilds has been initialized")


@client.command(name="shutdown", help="Stoppt den Bot")
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await client.close()


@client.command(name="RandomJoke", help="Gibt dir ein zufälligen schlechten Witz", usage="")
async def joke(ctx):
    await ctx.send(util_service.random_joke())


@client.command(name="JoinMe", help="Tritt deinem jeweiligen Voicechannel bei")
async def join_me(ctx):
    await ctx.send("Noch kann ich nicht dir beitreten... aber Bald ;) ")


@client.command(name="choco", help="SCHOKODRINK FÜR IMMER")
async def choco(ctx):
    await ctx.send("Schokodrink gerade noch in Lieferung. Aber bald möglich :chocolate_bar:")


@client.command(name="ContactOwner", help="Sendet Nachricht an den Entwickler")
async def contact(ctx, *, arg):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="StartProt", help="Speichert alle Nachrichten die folgen")
async def protocol(ctx):
    global protocolBool
    protocolBool = True
    await ctx.send("Protokoll wurde gestartet... [Achtung, alle jetzt gesendeten Nachrichten werden gespeichert!]")


@client.command(name="GetProt", help="Gibt alle Nachrichten aus, die gespeichert wurden")
async def get_protocol(ctx):
    await ctx.send(str(database_utils.get_all(Message)))

@client.command(name="StopProt", help="Stoppt die begonnene Protokollierung")
async def get_protocol(ctx):
    global protocolBool
    protocolBool = False
    await ctx.send("Protokoll wurde gestoppt")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Es scheint ein Argument zu fehlen, probiere nochmal mit: ***f!_[befehl] [message]***")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if protocolBool:
        message = Message(guild=msg.guild.id, channel=msg.channel.id, author=msg.author.name, message=msg.content)
        logging.info(
            f'({msg.created_at()})-({msg.guild.name})-({msg.channel.name})-[{msg.author.name}]: {msg.content}')
        database_utils.add(message)

    await client.process_commands(msg)
