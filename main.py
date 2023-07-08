import os
import json
import discord
from discord.ext import commands

# Load config data from file
with open('config.json') as f:
    config = json.load(f)

# Define intents object
intents = discord.Intents.all()

# Create instance of bot
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Bot event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command
@bot.command()
async def ping(ctx):
    await ctx.send('Bong!')

# Welcome message
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}")

# Run bot
bot.run(config["token"])