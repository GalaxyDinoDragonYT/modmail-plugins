import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx, *, message):
        channel = 
       
def setup(bot):
    bot.add_cog(report(bot))
