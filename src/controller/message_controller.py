import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import os

from src.controller import util_service
from src.database import database_utils
from src.models.schemas import Message

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


@client.command(name="shutdown", help="Stoppt den Bot")
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await client.close()


@client.command(name="RandomJoke", help="Gibt dir ein zufälligen schlechten Witz", usage="")
async def joke(ctx):
    await ctx.send(util_service.random_joke())


@client.command(name="test", help="Test befehl")
async def test(ctx):
    await ctx.send("Moin")


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


@client.command(name="ProtocolTest", help="Speichert alle Nachrichten die folgen")
async def protocol(ctx):
    global protocolBool
    protocolBool = True
    await ctx.send("Protocol started...")


@client.command(name="getProt")
async def get_protocol(ctx):
    await ctx.send(str(database_utils.get_all(Message)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Es scheint ein Argument zu fehlen, probiere nochmal mit: ***f!_[befehl] [message]***")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if protocolBool:
        message = Message(guild=msg.guild.name, channel=msg.channel.name, author=msg.author.name, message=msg.content)
        logging.info(
            f'({message.timestamp})-({message.guild})-({message.channel})-[{message.author}]: {message.message}')
        database_utils.add(message)

    await client.process_commands(msg)
