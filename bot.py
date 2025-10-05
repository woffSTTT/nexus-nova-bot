import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} è online!")

bot.load_extension("cogs.moderation")
bot.load_extension("cogs.logging")

bot.run(config["token"])
