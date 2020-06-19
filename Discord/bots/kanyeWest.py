# kanyeWest.py
import os
import random
import requests
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quote = requests.get('https://api.kanye.rest?format=text').text

    if message.content.lower() == 'tell me kanye':
        await message.channel.send(quote)

client.run(TOKEN)