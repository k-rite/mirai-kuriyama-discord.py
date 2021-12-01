import os
import discord #pip install discord
import config
import random
from discord import Game
from discord.ext import commands
from keep_alive import keep_alive
from discord.ext.commands import bot
import logging

#setting up discord logging to logging file
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#aligning the bot with discord.py features
Intents = discord.Intents.all()
prefixes = config.prefixes
Bot = commands.Bot(command_prefix=prefixes, intents=Intents)


#SETTING UP COGS
@Bot.command()
async def load(ctx, extension):
    Bot.load_extension(f'cogs.{extension}')

@Bot.command()
async def unload(ctx, extension):
    Bot.unload_extension(f'cogs.{extension}')
#AUTO Start loading all cogs from cog folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    Bot.load_extension(f'cogs.{filename[:-3]}')


#ping cmd
@Bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!! My heart is beating rn at {round(Bot.latency * 1000)}ms')
    print("ping cmd is used")

#a random custom cmd
@Bot.command()
async def owner(ctx):
    await ctx.send("UwU.... <@409340532675051531>")
    print("ping cmd is used")


#online checking 
@Bot.event
async def on_ready():
  general_channel = Bot.get_channel(897421298244927488)
  await general_channel.send(f'I am ON, Also Alert Krite if you see me running for a long time, <@409340532675051531> with {round(Bot.latency * 1000)}ms')
  print("I am on")

#some alignment for replit
keep_alive() # calls the keep alive function.
Token = os.environ['.env'] 
#If you dont want to setup env file or on safe network then jus remove "os.environ" line and add bot token in Bot.run("token_here")
Bot.run(Token)