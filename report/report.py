import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx, user: discord.Member, reason:str, *, proof:str):
        reports_channel = self.bot.get_channel(822612395516100618)
        embed = discord.Embed(title="New report", description=f'{ctx.author.mention} is reporting {user.mention} for {reason} \n Proof: {proof}')
        await reports_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(report(bot))
