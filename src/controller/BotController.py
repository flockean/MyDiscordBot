import logging
import discord
import os
from dotenv import load_dotenv
import src.handler.AiHandler as AiHandler
from discord.ext import commands

# Generate Discord-Bot client
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='f!')

logging.basicConfig(level=logging.INFO)


def start_bot():
    load_dotenv()

    # LogIn OpenAi ApiKey
    AiHandler.log_in_api(os.getenv('gpt_key'))
    # Start the bot
    bot.run(os.getenv('dc_key'))


@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


@bot.event
async def on_ready():
    print(f'Bot ist nun online: {bot.user.name}')


@bot.command()
async def hallo(ctx):
    await ctx.send('Hallo!')


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    logging.info("[" + str(msg.author) + "] " + msg.content)

    #
    if msg.content.startswith('C:'):
        question = msg.content
        answer = AiHandler.generate_completion(question)

        for part in answer:
            logging.info("text-davinci-003: " + part)
            await msg.channel.send(part)
    await bot.process_commands(msg)
