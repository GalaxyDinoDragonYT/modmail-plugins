import discord
from discord import *
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def newEmbed(self, ctx, title1, *, description1):
       await ctx.send(embed=discord.Embed(title=title, description=description1).set_author(name=ctx.author.display_name)

    
def setup(bot):
    bot.add_cog(embed(bot))
