import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(config["log_channel_id"])
        embed = discord.Embed(title="Messaggio Eliminato", description=message.content, color=discord.Color.dark_red())
        embed.set_author(name=message.author)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Logging(bot))
