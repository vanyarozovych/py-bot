import discord
from discord.ext import commands
import json

# Load config data from file
with open('config.json') as f:
    config = json.load(f)

# Create instance of bot
bot = commands.Bot(command_prefix=config["prefix"])

# Bot event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command
@bot.command()
async def ping(ctx):
    await ctx.send('Bong!')

# Run bot
bot.run(config["token"])