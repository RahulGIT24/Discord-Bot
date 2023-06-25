import discord
import os
import openai
from dotenv.main import load_dotenv
load_dotenv()

apiKey = os.environ['API_KEY']
token = os.environ['TOKEN']

openai.api_key = apiKey

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.mentions:
        if message.mentions[0] == client.user:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.content,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            await message.channel.send(response.choices[0].text)

client.run(token)
