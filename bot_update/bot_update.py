import discord
from discord.ext import commands

class botupdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx, *, message):
        channel = self.bot.get_channel(name="bot_updates")
        await channel.send(embed=discord.Embed(title="New bot upbate", description=message))
       
def setup(bot):
    bot.add_cog(botupdate(bot))
