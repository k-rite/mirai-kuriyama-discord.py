import discord
from discord.ext import commands
from discord import Game
class game(commands.Cog):
  def __init__(self, Bot):
    self.bot = Bot
#jus a comfy seperate cog to change game status, will add versions setup nd other backend codes here
  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="KRITE DYING VOL 79"))
    print('Game status is changed')


def setup(bot):
  bot.add_cog(game(bot))