import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def request(self, ctx, role):
        snr_guild = 815707057944133643
        if role == "snr" or "s&r":
       
def setup(bot):
    bot.add_cog(report(bot))
