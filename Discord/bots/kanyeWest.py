# kanyeWest.py
import os
import random
import requests
import random

from discord.ext import commands
from dotenv import load_dotenv

# Loads Discord keys using dotenv module
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

# Define prefix which will be used to call bot for action.
bot = commands.Bot(command_prefix='!', description='Kanye West himself!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Will respond to the command by getting a quote from Kanye REST API
# and posting as a message in the channel
@bot.command(name='preach', help='-Kanye will share his wisdom.')
async def kanye_wisdom(ctx):
    quote = requests.get('https://api.kanye.rest?format=text').text
    await ctx.send(quote)

# Bot prints Kanye West's bio.
@bot.command(name='bio', help='-Kanye will tell about himself')
async def kanye_bio(ctx):
    await ctx.send('I\'m an American rapper, singer, songwriter, record producer, composer, entrepreneur and fashion designer.')


bot.run(TOKEN)