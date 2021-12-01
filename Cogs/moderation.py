from operator import mod
import discord
from discord.ext import commands
from discord import Game
import os
import logging

#a seperate cog for moderation commands, more will be added soon.
class moderation(commands.Cog):
    def __init__(self, Bot):
        self.bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('moderation.py is loaded')


    @commands.command(aliases=['remove', 'delete'])
    async def purge(self, ctx, number: int):
        try:
            if ctx.message.author.guild_permissions.administrator:
                deleted = await ctx.channel.purge(limit=number)
                print('Deleted {} message(s)'.format(len(deleted)))
                logger.info('Deleted {} message(s)'.format(len(deleted)))

            else:
                await ctx.send(":x: **An unknown permission occurred.")
        except:
            await ctx.send(":x: **An unknown error occurred.")

#    @commands.command()
 #   async def roles(self, ctx):
  #      """All the roles in the server."""
  #      roles = ctx.message.guild.roles
   #     result = "**The roles on this server are: **"
   #     for role in roles:
    #        result += role.name + ", "
     #   await ctx.send(result)
      #  print(roles)

    @commands.command()
    async def say(self, ctx, *, arg=""):
        """Gives you a link to the GitHub website."""
        if arg == "":
            await ctx.send(f'{ctx.message.author.mention} Tell me what to say!')
        elif len(arg) > 50:
            await ctx.send(f"{ctx.message.author.mention} That's too long!")
        else:
            await ctx.message.delete()
            await ctx.send(f"```{arg}```")

    @commands.command(aliases=["fancy"])
    async def fancify(self, ctx, *, text):
        """Gives you a link to the GitHub website."""
        try:

            def strip_non_ascii(string):
                """Returns the string without non ASCII characters."""
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)

            text = strip_non_ascii(text)
            if len(text.strip()) < 1:
                return await Bot.ctx.send(":x: ASCII characters only please!")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await ctx.send(output)

        except:
            await ctx.send(":x: **An unknown error occurred.")

    @commands.command()
    async def bigtext(self, ctx, *, text):
        """Gives you a link to the GitHub website."""
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="big") +
                           "```")
        except:
            await ctx.send(":x: **An unknown error occurred.")

    @commands.command(aliases=['game', 'presence'])
    async def setgame(self, ctx, *args):
        """Gives you a link to the GitHub website."""
        try:
            if ctx.message.author.guild_permissions.administrator:
                setgame = ' '.join(args)
                await Bot.change_presence(status=discord.Status.online,
                                          activity=discord.Game(setgame))
                await ctx.send(":ballot_box_with_check: Game name set to: `" +
                               setgame + "`")
                print("Game set to: `" + setgame + "`")
            else:
                await ctx.send(":x: **An unknown permission occurred.")
        except:
            await ctx.send(":x: **An unknown error occurred.")

    @commands.command()
    async def serverlist(self, ctx):
        """Gives you a link to the GitHub website."""
        x = ', '.join([str(server) for server in self.bot.guilds])
        y = len(self.bot.guilds)
        print("Server list: " + x)
        if y > 40:
            embed = discord.Embed(
                title="Currently active on " + str(y) + " servers:",
                description=":x: **An unknown error occurred." +
                "```json\nCan't display more than 40 servers!```",
                colour=0xFFFFF)
            return await ctx.send(embed=embed)
        elif y < 40:
            embed = discord.Embed(title="Currently active on " + str(y) +
                                  " servers:",
                                  description="```json\n" + x + "```",
                                  colour=0xFFFFF)
            return await ctx.send(embed=embed)

    #@commands.command()
    #async def getbans(ctx):
    # """Lists all banned users on the current server."""
    #if ctx.message.author.guild_permissions.ban_members:
    # x = await ctx.message.guild.bans()
    #x = '\n'.join([str(y.user) for y in x])
    #embed = discord.Embed(title="List of Banned Members", description=x, colour=0xFFFFF
    #return await ctx.send(embed=embed)
    #else:
    #await ctx.send(":x: **An unknown permission occurred.")

    @commands.command(aliases=['user'])
    async def info(self, ctx, user: discord.Member):
        """Gives you a link to the GitHub website."""
        embed = discord.Embed(title="User profile: " + user.name,
                              colour=user.colour)
        embed.add_field(name="Name:", value=user.name)
        embed.add_field(name="ID:", value=user.id)
        embed.add_field(name="Status:", value=user.status)
        embed.add_field(name="Highest role:", value=user.top_role)
        embed.add_field(name="Joined:", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['gh', 'code', 'website'])
    async def github(self, ctx):
        """Gives you a link to the GitHub website."""
        await ctx.send("**GitHub:** soon added on https://github.com/k-rite")


def setup(bot):
    bot.add_cog(moderation(bot))
