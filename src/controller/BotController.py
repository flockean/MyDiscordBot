import logging
import discord
import os
from dotenv import load_dotenv
import src.handler.AiHandler as AiHandler

# Generate Discord-Bot client
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

logging.basicConfig(level=logging.INFO)


def start_bot():
    load_dotenv()

    # LogIn OpenAi ApiKey
    AiHandler.log_in_api(os.getenv('gpt_key'))
    # Start the bot
    bot.run(os.getenv('dc_key'))


@bot.event
async def on_ready():
    logging.info("Bot is online")


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    logging.info("[" + str(msg.author) + "]," + msg.content)

    #
    if msg.content.startswith('C:'):
        question = msg.content
        answer = AiHandler.generate_completion(question)


        for part in answer:
            logging.info("text-davinci-003: " + part)
            await msg.channel.send(part)

