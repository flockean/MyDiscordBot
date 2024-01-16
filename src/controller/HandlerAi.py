import logging
import os
from openai import OpenAI
from dotenv import load_dotenv
from .Util import *
import json


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)




def split_string(inp_string):
    return [inp_string[i:i + 2000] for i in range(0, len(inp_string), 2000)]


def generate_completion_text003(question):
    prompt = f"Question: {question}\nAnswer:"
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt
    )
    logging.info(response)
    return response


class Compo:
    with open(file_path("gptPrompt.json"), "r") as file:
        pomp = json.load(file)
    msg = pomp["Snowflake"]


def generate_completion_gpt4(chat, question):
    chat.msg.append({"role": "user", "content": question})
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=chat.msg
        )
    except Exception:
        return "Error, Noch keine Rechte zum BigBrain ;("

    return response.choices[0].message.content


def generate_completion_gpt3turbo(chat, question):
    chat.msg.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat.msg
    )
    logging.info(response.choices[0].message.content)
    logging.info(response.usage)
    return response.choices[0].message.content
