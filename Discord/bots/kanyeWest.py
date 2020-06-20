# kanyeWest.py
import os
import random
import requests
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

bot = commands.Bot(command_prefix='!', description='Kanye West himself!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='preach', help='-Kanye will share his wisdom.')
async def kanye_wisdom(ctx):
    quote = requests.get('https://api.kanye.rest?format=text').text
    await ctx.send(quote)

@bot.command(name='bio', help='-Kanye will tell about himself')
async def kanye_bio(ctx):
    await ctx.send('I\'m an American rapper, singer, songwriter, record producer, composer, entrepreneur and fashion designer.')


bot.run(TOKEN)