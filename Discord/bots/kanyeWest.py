# kanyeWest.py
import os
import random
import requests
import random
import json
import datetime
import dadJokes as dj
import descriptions as d
from discord.ext import commands, timers
from dotenv import load_dotenv

# Loads Discord keys using dotenv module
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

# Defines prefix which will be used to call bot for action.
bot = commands.Bot(command_prefix='!', description='Kanye West himself!')
bot.timer_manager = timers.TimerManager(bot)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

"""
Gets a quote from Kanye REST API and posts in the channel
"""
@bot.command(name='preach', help='-Kanye shares his wisdom.')
async def kanye_wisdom(ctx):
    quote = requests.get('https://api.kanye.rest?format=text').text
    await ctx.send(quote)

"""Prints Kanye West's bio."""
@bot.command(name='bio', help='-Learn who is Kanye from Kanye')
async def kanye_bio(ctx):
    await ctx.send('I\'m an American rapper, singer, songwriter, record producer, composer, entrepreneur and fashion designer and Special guest @OnlineMCIT.')

"""Tells a dad joke. Takes string(s) as an argument."""
@bot.command(name='joke', help='-Kanye tells you a dad-joke based on a given word(s)')
async def kanye_joke(ctx, *args):
    await ctx.send(dj.choosing_joke(args))

"""Kanye provides information regarding the programm."""
@bot.command(name='demographics', help='-Gives the Student Demographics')
async def deadline(ctx):
    await ctx.send(
        'Countries Represented: 32' \
        + '\nUS States/Territories Represented: 41' \
        + '\nAge range: 20s-60s' \
        + '\nUS Citizens: 49%' \
        + '\nInternational Students: 51%' \
        + '\nWomen: 38%' \
        + '\nMen: 62%' \
        + '\nTotal Program Enrollment: 626' \
        + '\nIncoming Class Size: 250-350'
    )

"""Provides info about the courses"""
@bot.command(name='list', help='-Lists core and currently available elective courses')
async def courses(ctx):
    await ctx.send(
        'Core:\n' \
            + 'CIT 591 Introduction to Software Development;\n' \
            + 'CIT 592 Mathematical Foundations of Computer Science;\n' \
            + 'CIT 593 Introduction to Computer Systems;\n' \
            + 'CIT 594 Data Structures & Software Design;\n' \
            + 'CIT 595 Computer Systems Programming;\n' \
            + 'CIT 596 Algorithms & Computation;\n' \
        + 'Electives:\n' \
            + 'CIS 515 Fundamentals of Linear Algebra & Optimization (Math for ML);\n' \
            + 'CIS 547 Software Analysis;\n' \
            + 'CIS 549 Wireless Communications for Mobile Networks and Internet of Things;\n' \
            + 'CIS 550 Database & Information Systems;\n' \
            + 'CIS 581 Computer Vision & Computational Photography;\n' \
            + 'ESE 542 Statistics for Data Science;'
    )

@bot.command(name='course', help='-Gives description of a specific course. Exmaple: !course cit591')
async def course_info(ctx, course_number):
    if course_number.lower() == 'cit591':
        await ctx.send(d.cit591())
    elif course_number.lower() == 'cit592':
        await ctx.send(d.cit591())
    elif course_number.lower() == 'cit593':
        await ctx.send(d.cit593())
    elif course_number.lower() == 'cit594':
        await ctx.send(d.cit594())
    elif course_number.lower() == 'cit595':
        await ctx.send(d.cit595())
    elif course_number.lower() == 'cit596':
        await ctx.send(d.cit596())
    elif course_number.lower() == 'cis515':
        await ctx.send(d.cis515())
    elif course_number.lower() == 'cis547':
        await ctx.send(d.cis547())
    elif course_number.lower() == 'cis549':
        await ctx.send(d.cis549())
    elif course_number.lower() == 'cis550':
        await ctx.send(d.cis550())
    elif course_number.lower() == 'cis581':
        await ctx.send(d.cis581())
    elif course_number.lower() == 'ese542':
        await ctx.send(d.ese542())

@bot.command(name='remind', help='-Sets up reminder. The date must be in ``Y/M/D`` format.')
async def remind(ctx, time, *, text):
    try:
        date = datetime.datetime(*map(int, time.split("/")))
        await ctx.send(f"I'll remind you: *{text}* on: {date}!")
        bot.timer_manager.create_timer("reminder", date, args=(ctx.channel.id, ctx.author.id, text))
    except:
        await ctx.send('Error: after command first indicate time, then reminder msg. ' \
            + 'The time format should be in 24-h format with `Y/M/D/h/m/s`, where `h/m/s` is optional')

@bot.event
async def on_reminder(channel_id, author_id, text):
    channel = bot.get_channel(channel_id) # grab the channel where bot will post the reminder
    user = bot.get_user(author_id) # grab the user where bot will post the reminder
    await channel.send(f"Hey, <@{author_id}>, remember to: **{text}**")
    await user.send(f"Hey, <@{author_id}>, remember to: **{text}**")

bot.run(TOKEN)