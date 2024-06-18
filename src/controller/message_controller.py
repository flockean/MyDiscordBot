import datetime
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import os

from src.controller import util_service
from src.database import database_utils
from src.models.schemas import Message, Guild, GuildChannel, DMMessage
from src.service.api import get_image

# Generate Discord-Bot client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="f!_")
logging.basicConfig(level=logging.INFO)
client.remove_command('help')

protocolBool = False


def start_bot():
    load_dotenv()
    # Start the bot
    client.remove_command('help')
    client.run(os.getenv('DISCORD_BOT'))


@client.event
async def on_ready():
    logging.info("BotStats: " + str(client.user) + " Id: " + str(client.application_id))
    for guild in client.guilds:
        database_utils.add(Guild(id=guild.id, name=guild.name))
        for channel in guild.text_channels:
            database_utils.add(GuildChannel(id=channel.id, name=channel.name, guild_id=guild.id))
    logging.info("Guilds has been initialized")


@client.command(name="help", help="Bessere version von help")
async def help(ctx):
    helptext = ""
    for command in client.commands:
        helptext += f"> `{command}` \n > {command.help}\n > \n"
    await ctx.send(f'> ### Hier sind alle nutzbaren commands \n' + f'{helptext}')


@client.command(name="shutdown", help="Stoppt den Bot")
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await client.close()


@client.command(name="MessageToHell", help="Sendet eine Nachricht in die Dunkelheit", usage="porn")
async def message_to_hell(ctx, *, arg):
    user = await client.fetch_user(227866227471679488)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="RandomJoke", help="Gibt dir ein zufälligen schlechten Witz")
async def joke(ctx):
    await ctx.send(util_service.random_joke())


@client.command(name="neko", help="Gibt ein random Neko Bild (Warnung kann nsfw sein)")
async def neko(ctx):
    await ctx.send(get_image(nsfw=False))


@client.command(name="nsfw", help="Gibt ein random Nsfw Bild")
async def nsfw(ctx):
    await ctx.send(get_image(nsfw=True))


@client.command(name="ContactOwner", help="Sendet Nachricht an den Entwickler")
async def contact(ctx, *, arg):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="private", help="Nur Nutzung vom Owner")
async def private(ctx):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(str(database_utils.get_all(DMMessage)))
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="StartProtokoll", help="Speichert alle Nachrichten die folgen")
async def protocol(ctx):
    global protocolBool
    protocolBool = True
    await ctx.send("Protokoll wurde gestartet... [Achtung, alle jetzt gesendeten Nachrichten werden gespeichert!]")


@client.command(name="GetProtokoll", help="Gibt alle Nachrichten aus, die gespeichert wurden")
async def get_protocol(ctx):
    await ctx.send(str(database_utils.get_all(Message)))


@client.command(name="StopProtokoll", help="Stoppt die begonnene Protokollierung")
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
        if msg.guild == None:
            return
        message = Message(guild=msg.guild.id, channel=msg.channel.id, author=msg.author.name, message=msg.content)
        logging.info(
            f'({msg.created_at()})-({msg.guild.name})-({msg.channel.name})-[{msg.author.name}]: {msg.content}')
        database_utils.add(message)
    if msg.guild == None:
        database_utils.add(DMMessage(author=msg.author.name, content=msg.content))
    logging.info(f'{msg.author}: {msg.content}')
    await client.process_commands(msg)
