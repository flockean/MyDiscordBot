import datetime
import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.controller import util_service
from src.controller.util_service import Category
from src.database import database_utils
from src.models.schemas import Message, DMMessage
from src.service.api import get_image, neko_best

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
    client.run(os.getenv('DISCORD_BOT'))


@client.event
async def on_ready():
    logging.info("BotStats: " + str(client.user) + " Id: " + str(client.application_id))
    logging.info("Guilds has been initialized")


@client.command(name="help", help="Bessere version von help", usage=Category.settings)
async def help(ctx):
    helptext = ""
    for category in Category:
        helptext += f'\n > ### {category.value} \n > '
        for command in client.commands:
            if command.usage == category:
                helptext += f'`{command}` '
    await ctx.send(f'> ### Hier sind alle nutzbaren commands \n > {helptext}')


@client.command(name="shutdown", help="Stoppt den Bot", usage=Category.settings)
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await client.close()


@client.command(name="MessageToHell", help="Sendet eine Nachricht in die Dunkelheit", usage=Category.settings)
async def message_to_hell(ctx, *, arg):
    user = await client.fetch_user(227866227471679488)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="RandomJoke", help="Gibt dir ein zufälligen schlechten Witz", usage=Category.rest)
async def joke(ctx):
    await ctx.send(util_service.random_joke())


@client.command(name="nsfw", help="Gibt ein random Nsfw Bild", usage=Category.nsfw)
async def nsfw(ctx):
    await ctx.send("Leider gerade kaputt ;(")


@client.command(name="ContactOwner", help="Sendet Nachricht an den Entwickler", usage=Category.settings)
async def contact(ctx, *, arg):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="private", help="Nur Nutzung vom Owner", usage=Category.settings)
async def private(ctx):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(str(database_utils.get_all(DMMessage)))
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.command(name="StartProtokoll", help="Speichert alle Nachrichten die folgen", usage=Category.management)
async def protocol(ctx):
    global protocolBool
    protocolBool = True
    await ctx.send("Protokoll wurde gestartet... [Achtung, alle jetzt gesendeten Nachrichten werden gespeichert!]")


@client.command(name="GetProtokoll", help="Gibt alle Nachrichten aus, die gespeichert wurden",
                usage=Category.management)
async def get_protocol(ctx):
    msg_list = ""
    for message in database_utils.get_all(Message):
        msg_list += f'{message}'
    await ctx.send(msg_list)


@client.command(name="StopProtokoll", help="Stoppt die begonnene Protokollierung", usage=Category.management)
async def get_protocol(ctx):
    global protocolBool
    protocolBool = False
    await ctx.send("Protokoll wurde gestoppt")


@client.command(usage=Category.interaction)
async def neko(ctx):
    await ctx.send(neko_best("neko"))


@client.command(usage=Category.interaction)
async def waifu(ctx):
    await ctx.send(neko_best("waifu"))


@client.command(usage=Category.interaction)
async def husbando(ctx):
    await ctx.send(neko_best("husbando"))


@client.command(usage=Category.interaction)
async def kitsune(ctx):
    await ctx.send(neko_best("kitsune"))


@client.command(usage=Category.interaction)
async def lurk(ctx):
    await ctx.send(neko_best("lurk"))


@client.command(usage=Category.interaction)
async def shoot(ctx):
    await ctx.send(neko_best("shoot"))


@client.command(usage=Category.interaction)
async def sleep(ctx):
    await ctx.send(neko_best("sleep"))


@client.command(usage=Category.interaction)
async def shrug(ctx):
    await ctx.send(neko_best("shrug"))


@client.command(usage=Category.interaction)
async def stare(ctx):
    await ctx.send(neko_best("stare"))


@client.command(usage=Category.interaction)
async def wave(ctx):
    await ctx.send(neko_best("wave"))


@client.command(usage=Category.interaction)
async def poke(ctx):
    await ctx.send(neko_best("poke"))


@client.command(usage=Category.interaction)
async def smile(ctx):
    await ctx.send(neko_best("smile"))


@client.command(usage=Category.interaction)
async def peck(ctx):
    await ctx.send(neko_best("peck"))


@client.command(usage=Category.interaction)
async def wink(ctx):
    await ctx.send(neko_best("wink"))


@client.command(usage=Category.interaction)
async def blush(ctx):
    await ctx.send(neko_best("blush"))


@client.command(usage=Category.interaction)
async def smug(ctx):
    await ctx.send(neko_best("smug"))


@client.command(usage=Category.interaction)
async def tickle(ctx):
    await ctx.send(neko_best("tickle"))


@client.command(usage=Category.interaction)
async def yeet(ctx):
    await ctx.send(neko_best("yeet"))


@client.command(usage=Category.interaction)
async def think(ctx):
    await ctx.send(neko_best("think"))


@client.command(usage=Category.interaction)
async def highfive(ctx):
    await ctx.send(neko_best("highfive"))


@client.command(usage=Category.interaction)
async def feed(ctx):
    await ctx.send(neko_best("feed"))


@client.command(usage=Category.interaction)
async def bite(ctx):
    await ctx.send(neko_best("bite"))


@client.command(usage=Category.interaction)
async def bored(ctx):
    await ctx.send(neko_best("bored"))


@client.command(usage=Category.interaction)
async def nom(ctx):
    await ctx.send(neko_best("nom"))


@client.command(usage=Category.interaction)
async def yawn(ctx):
    await ctx.send(neko_best("yawn"))


@client.command(usage=Category.interaction)
async def facepalm(ctx):
    await ctx.send(neko_best("facepalm"))


@client.command(usage=Category.interaction)
async def cuddle(ctx):
    await ctx.send(neko_best("cuddle"))


@client.command(usage=Category.interaction)
async def kick(ctx):
    await ctx.send(neko_best("kick"))


@client.command(usage=Category.interaction)
async def happy(ctx):
    await ctx.send(neko_best("happy"))


@client.command(usage=Category.interaction)
async def hug(ctx):
    await ctx.send(neko_best("hug"))


@client.command(usage=Category.interaction)
async def baka(ctx):
    await ctx.send(neko_best("baka"))


@client.command(usage=Category.interaction)
async def pat(ctx):
    await ctx.send(neko_best("pat"))


@client.command(usage=Category.interaction)
async def nod(ctx):
    await ctx.send(neko_best("nod"))


@client.command(usage=Category.interaction)
async def nope(ctx):
    await ctx.send(neko_best("nope"))


@client.command(usage=Category.interaction)
async def kiss(ctx):
    await ctx.send(neko_best("kiss"))


@client.command(usage=Category.interaction)
async def dance(ctx):
    await ctx.send(neko_best("dance"))


@client.command(usage=Category.interaction)
async def punch(ctx):
    await ctx.send(neko_best("punch"))


@client.command(usage=Category.interaction)
async def handshake(ctx):
    await ctx.send(neko_best("handshake"))


@client.command(usage=Category.interaction)
async def slap(ctx):
    await ctx.send(neko_best("slap"))


@client.command(usage=Category.interaction)
async def cry(ctx):
    await ctx.send(neko_best("cry"))


@client.command(usage=Category.interaction)
async def pout(ctx):
    await ctx.send(neko_best("pout"))


@client.command(usage=Category.interaction)
async def handhold(ctx):
    await ctx.send(neko_best("handhold"))


@client.command(usage=Category.interaction)
async def thumbsup(ctx):
    await ctx.send(neko_best("thumbsup"))


@client.command(usage=Category.interaction)
async def laugh(ctx):
    await ctx.send(neko_best("laugh"))


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
            f'({datetime.datetime.now()})-({msg.guild.name})-({msg.channel.name})-[{msg.author.name}]: {msg.content}')
        database_utils.add(message)
    if msg.guild is None:
        database_utils.add(DMMessage(author=msg.author.name, content=msg.content))
    logging.info(f'{msg.channel.name}:{msg.author}: {msg.content}')
    await client.process_commands(msg)
