import discord
from discord.ext import commands
import random
import config #must sync config file before loading up cogs
#setting up cog with name"action" here
class action(commands.Cog):
  def __init__(self, Bot):
    self.bot = Bot

#printing in prompt to know cog is in sync
  @commands.Cog.listener()
  async def on_ready(self):
    print('action.py cog loaded')
#sorry cmd
  @commands.command(aliases=['zory'])
  async def sorry(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "sorry to " f"{str(member.name)}"
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.sorrygif))
    await ctx.send(embed = hero)

#sus
  @commands.command()
  async def sus(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "sus " f"{str(member.name)}"
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.susgifs))
    await ctx.send(embed = hero)


#bruh
  @commands.command()
  async def bruh(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "bruh " f"{str(member.name)}"
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.bruhgifs))
    await ctx.send(embed = hero)


#bye
  @commands.command(aliases=['by'])
  async def bye(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "byez " f"{str(member.name)}"
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.byegifs))
    await ctx.send(embed = hero)

#cuddle commands
  @commands.command()
  async def cuddle(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "cuddles " f"{str(member.name)}"
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.cuddlegifs))
    await ctx.send(embed = hero)

#gg
  @commands.command()
  async def gg(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "gg " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.gggifs))
    await ctx.send(embed = hero)

#gm
  @commands.command(aliases=['gm','ohayo'])
  async def goodmorning(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*goodmorning* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.gmgifs))
    await ctx.send(embed = hero)

#gn
  @commands.command(aliases=['gn'])
  async def goodnight(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*goodnight* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.gngifs))
    await ctx.send(embed = hero)

#hbd
  @commands.command(aliases=['hbd'])
  async def happybirthday(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*whishes Happy Birthday to* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.hbdgifs))
    await ctx.send(embed = hero)

#highfive
  @commands.command()
  async def highfive(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*highfives* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.highfivegifs))
    await ctx.send(embed = hero)

#hug
  @commands.command()
  async def hug(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*hugs* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.huggif))
    await ctx.send(embed = hero)

#kick
  @commands.command()
  async def kick(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*kicks* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.kickgifs))
    await ctx.send(embed = hero)

#lick
  @commands.command()
  async def lick(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*licks* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.lickgif))
    await ctx.send(embed = hero)

#punch
  @commands.command()
  async def punch(self, ctx, member: discord.Member):
   
   embedtitle =  f"{str(ctx.author.name)} " "*punches* " f"{str(member.name)}"
   rgif = random.choice(config.punchgifs)
   embedmsg = discord.Embed(title = embedtitle, color = 0x000000)
   embedmsg.set_image(url = rgif)
   await ctx.message.channel.send(embed = embedmsg)

#shoot
  @commands.command()
  async def shoot(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*shoots* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.shootgifs))
    await ctx.send(embed = hero)

#slap
  @commands.command()
  async def slap(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*slaps* " f"{str(member.name)}"
    
    rgif = random.choice(config.slapgifs)
    embedmsg = discord.Embed(title = embedtitle, color = 0x000000)
    embedmsg.set_image(url = rgif)
    await ctx.message.channel.send(embed = embedmsg)

#thankyou
  @commands.command(aliases=['ty'])
  async def thankyou(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*thanks* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.thankyougifs))
    await ctx.send(embed = hero)


#vibe
  @commands.command()
  async def vibe(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*vibing* with " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.vibegifs))
    await ctx.send(embed = hero)
#wtf
  @commands.command(aliases=['f'])
  async def wtf(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "**WTF** " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.wtfgifs))
    await ctx.send(embed = hero)

#tired
  @commands.command()
  async def tired(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "tired by  " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.tiredgifs))
    await ctx.send(embed = hero)

#confused
  @commands.command()
  async def confused(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "*confused by* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.confusedgifs))
    await ctx.send(embed = hero)
#idk

  @commands.command(aliases=['dunno'])
  async def idk(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "DUNNO!! " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.idkgifs))
    await ctx.send(embed = hero)

#disgust

  @commands.command(aliases=['agh'])
  async def disgust(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "disgusted by " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.disgustgifs))
    await ctx.send(embed = hero)

#hungry
  @commands.command()
  async def hungry(self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)} " "hungry" f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.hungrygifs))
    await ctx.send(embed = hero)

#roll 
  @commands.command()
  async def roll (self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)}" " *rolling towards* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.rollgifs))
    await ctx.send(embed = hero)  

#jk
  @commands.command(aliases=['justkidding'])
  async def jk (self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)}" " *just kidding* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.jkgifs))
    await ctx.send(embed = hero)  


#handshake 
  @commands.command()
  async def handshake (self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)}" " *handshakes* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.handshakesgifs))
    await ctx.send(embed = hero)  



#pat 
  @commands.command()
  async def pat (self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)}" " *pats* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.patgifs))
    await ctx.send(embed = hero)  




#kill 
  @commands.command()
  async def kill (self, ctx, member: discord.Member):
    embedtitle = f"{str(ctx.author.name)}" " *kills* " f"{str(member.name)}"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.killgifs))
    await ctx.send(embed = hero)  



#mirai 
  @commands.command(aliases=['Mirai','whou','whoru'])
  async def mirai(self,ctx):
    embedtitle = "*blueshes..........*"
    
    hero = discord.Embed(title = embedtitle, colour = 0x000000)
    hero.set_image(url = random.choice(config.miraigifs))
    await ctx.send(embed = hero)


def setup(bot):
  bot.add_cog(action(bot))
