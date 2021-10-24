import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx, user: discord.Member, reason:str, *, proof:str):
        reports_channel = self.bot.get_channel(822612395516100618)
        embed = discord.Embed(title="New report", description=f'{ctx.author.mention} is reporting {user.mention} for {reason} \n\n Proof: {proof}')
        await reports_channel.send("<@&806462934111879209> <@&806462990005174302>",embed=embed)
        await ctx.send("Report sent!")
     
    @commands.command()
    async def appeal(self, ctx, punishment:str, reasonfor:str, *, appeal:str):
        appeals_channel = self.bot.get_channel(822612512942850059)
        embed = discord.Embed(title="New appeal", description=f'{ctx.author.mention} is appealing a {punishment} for {reasonfor} \n\n Appeal: {appeal}')
        await appeals_channel.send("<@&806462934111879209> <@&806462990005174302>",embed=embed)
        await ctx.send("Appeal sent!")

    @commands.command()
    async def feedback(self, ctx, stars: int, topic:str, *, description:str):
        reports_channel = self.bot.get_channel(806529349964005406)
        embed = discord.Embed(title="New feedback", description=f'User: {ctx.author.mention}\n\nStar Star rating: {stars}/5\n\nTopic:\n\n   {topic}\n\nExplanation:\n\n   {description}')
        await reports_channel.send(embed=embed)
        await ctx.send("Feedback sent!")
       
def setup(bot):
    bot.add_cog(report(bot))
