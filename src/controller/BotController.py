import discord
from discord.ext import commands

from .HandlerAi import *
from .Util import *

# Generate Discord-Bot client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="f!_")
logging.basicConfig(level=logging.INFO)


def start_bot():
    load_dotenv()
    # Start the bot
    client.run(os.getenv('DC_KEY'))


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
    await ctx.send(random_joke())


@client.command(name="test", help="Test befehl")
async def test(ctx):
    await ctx.send("Moin")

compo = Compo()


@client.command(name="JoinMe", help="Tritt deinem jeweiligen Voicechannel bei")
async def join_me(ctx):
    await ctx.send("Noch kann ich nicht dir beitreten... aber Bald ;) ")


@client.command(name="choco", help="SCHOKODRINK FÜR IMMER")
async def choco(ctx):
    await ctx.send("Schokodrink gerade noch in Lieferung. Aber bald möglich :chocolate_bar:")

@client.command(name="ConntactOwner", help="Sendet Nachricht an den Entwickler")
async def contact(ctx, *, arg):
    user = await client.fetch_user(343467598614233100)
    if user:
        await user.send(arg)
        await ctx.send("Nachricht gesendet")
    else:
        await ctx.send("Fehler beim senden, sorry ;(")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Es scheint ein Argument zu fehlen, probiere nochmal mit: ***f!_[befehl] [message]***")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith(f'<@{client.application_id}> '):
        await msg.channel.send(generate_completion_gpt3turbo(compo, msg.content))
    if "W5" in msg.content:
        await msg.channel.send("Geheiligt sei W5 und der Kult der ultimativen Reinigung. Möget ihr euer Leben des "
                               "Kultes widmen <a:pervblush:991058371387990057>")

    logging.info("[" + str(msg.author) + "] " + msg.content)

    await client.process_commands(msg)



