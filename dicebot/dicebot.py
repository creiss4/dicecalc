
import discord
from discord.ext import commands

intents = discord.Intents().all()

client = commands.Bot(command_prefix = "d!", case_insensitive = True, intents=intents)
#token contained in separate file, unique token that is required for the bot to run
token = open("token.txt", "r").read()

@client.event
async def on_ready():
    print("Ready")

@client.command()
async def foo(ctx):
    await ctx.send("I'm ready!")


client.run(token)