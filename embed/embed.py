import discord
import asyncio
from discord.ext import commands, tasks

class utility(commands.Cog):  
    def __init__(self, bot):
        self.bot = bot
        
        

def setup(bot):
    bot.add_cog(utility(bot))
