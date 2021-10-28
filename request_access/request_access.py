import discord
from discord import interactions
from discord.ext import commands

class request_access(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def request(self, ctx):
        all_give = 815668824656445470
        snr_guild = self.bot.get_guild(815707057944133643)
        snr_role = discord.utils.get(snr_guild.roles, id = "821389484339494932")
        snr_give = 815669285380292608
        #guide_guild = self.bot.get_guild(807134064322412555) 
        guide_role = 830627185554751509 
        guide_give = 815668898715926559
        wea_guild = self.bot.get_guild(819992511157239919)
        wea_role =  discord.utils.get(wea_guild.roles, id = "819995995986985010")
        wea_give = 815669020756934678
        wa_guild = self.bot.get_guild(806222338584477736)
        events_role = 817417302747119627
        events_give = 815670590127996968
        mod_role = 806324625784176682
        mod_give = 815669359472148480

        buttons = [create_button(style=ButtonStyle.green, label="WEA"),create_button(style=ButtonStyle.blue, label="WASR"), create_button(style=ButtonStyle.red, label="WAGS"),create_button(style=ButtonStyle.green, label="WA events"), create_button(style=ButtonStyle.blue, label="WA moderation")]
        action_row = create_actionrow(*buttons)

        await ctx.send(components=[action_row])

    
def setup(bot):
    bot.add_cog(request_access(bot))
