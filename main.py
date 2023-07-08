import os
import json
import discord
from discord.ext import commands
import requests

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
    await bot.change_presence(activity=discord.Game(name="🐍"))

# Ping -> Bong
@bot.command()
async def ping(ctx):
    await ctx.send('Bong!')

# Purge command !purge
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount + 1)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You have insufficient privileges to execute this command.')
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send('I do not have the necessary permissions to perform that task.')

# Check minecraft server status
@bot.command()
async def serverstatus(ctx):
    server = 'vanyarozovych.aternos.me:56613'
    response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
    data = response.json()
    if data['online']:
        message = f"✅ - Server `{server}` is online. There are currently `{data['players']['online']}`/`{data['players']['max']}` players online."
    else:
        message = f"❌ - Server `{server}` is offline."
    await ctx.send(message)

# Welcome message upon joining server
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}")

# Run bot
bot.run(config["token"])