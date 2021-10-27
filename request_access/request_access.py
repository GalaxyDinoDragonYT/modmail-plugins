import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def request(self, ctx, role):
        all_give = 815668824656445470
        snr_guild = self.bot.get_guild(815707057944133643)
        snr_role = 821389484339494932
        snr_give = 815669285380292608
        guide_guild = self.bot.get_guild(807134064322412555) 
        guide_role = 830627185554751509 
        guide_give = 815668898715926559
        wea_guild = self.bot.get_guild(819992511157239919)
        wea_role = 819995995986985010
        wea_give = 815669020756934678
        wa_guild = self.bot.get_guild(806222338584477736)
        events_role = 817417302747119627
        events_give = 815670590127996968
        mod_role = 806324625784176682
        mod_give = 815669359472148480
        if role == "snr" or "s&r":
            if ctx.author has snr_guild.get_role(snr_role):
                ctx.author.add_role(snr_give)
    
def setup(bot):
    bot.add_cog(report(bot))
