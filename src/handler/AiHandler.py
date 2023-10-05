import logging

import openai


def log_in_api(apikey):

    openai.api_key = apikey
    logging.info("apikey has been set")


def generate_completion(question):
    prompt = f"Question: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=4000,
    )
    answers = split_string(response.choices[0].text)
    return answers


def split_string(inp_string):
    return [inp_string[i:i + 2000] for i in range(0, len(inp_string), 2000)]
