import discord
from discord.ext import commands
from discord import Game
class cogtemplate(commands.Cog): #change class with your class name
  def __init__(self, Bot):
    self.bot = Bot
    #a sample on_ready() cmd.
  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="KRITE DYING VOL 79"))
    print('Game status is changed')
    
   #sample cog command
  @commands.command()
  async def ping(ctx):
    await ctx.send(f'Pong!! My heart is beating rn at {round(Bot.latency * 1000)}ms')
    print("ping cmd is used")

def setup(bot):
  bot.add_cog(cogtemplate(bot))#change cogtemplate with your cog name
