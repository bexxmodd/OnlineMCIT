# kanyeWest.py
import os
import random
import requests
import random
import json
import dadJokes as dj

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
@bot.command(name='preach', help='-Kanye shares his wisdom.')
async def kanye_wisdom(ctx):
    quote = requests.get('https://api.kanye.rest?format=text').text
    await ctx.send(quote)

# Bot prints Kanye West's bio.
@bot.command(name='bio', help='-Learn who is Kanye from Kanye')
async def kanye_bio(ctx):
    await ctx.send('I\'m an American rapper, singer, songwriter, record producer, composer, entrepreneur and fashion designer.')

# Kanye will tell a dad joke. Takes string(s) as an argument.
@bot.command(name='joke', help='-Kanye tells you a dad-joke based on a given word(s)')
async def kanye_joke(ctx, *args):
    await ctx.send(dj.choosing_joke(args))

bot.run(TOKEN)