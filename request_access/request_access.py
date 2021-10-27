import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def request(self, ctx, role):
        if role == "snr" or "s&r":
       
def setup(bot):
    bot.add_cog(report(bot))
