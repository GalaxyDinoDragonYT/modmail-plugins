import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.coll = bot.api.get_plugin_partition(self)
        self.bot = bot

    @commands.command()
    async def report(self, ctx):
        
       
def setup(bot):
    bot.add_cog(report(bot))
