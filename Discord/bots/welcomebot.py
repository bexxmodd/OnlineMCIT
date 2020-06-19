# bot.py
import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

@client.event

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    msg = f'Hello <@{member.id}>! Welcome to the UPenn Online MCIT Discord Server. Please head to the <#722617468622733385> and read the instructions to start using the server.'
    channel = client.get_channel(722612886924427357)
    await channel.send(msg)
    print(member.name + " was greeted")

@client.event
async def on_member_remove(member):
    print(member.name + " left the channel")
    msg = f'{member.name} left the server'
    channel = client.get_channel(723583513563234344)
    await channel.send(msg)

client.run(TOKEN)