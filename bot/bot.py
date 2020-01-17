import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
    print("bot is ready.")

@client.command()
async def sup_bian(ctx):
    await ctx.send('ello')

@client.command(aliases=['what_is_security'])
async def spor(ctx):
    await ctx.send('security is a process, not a product')

@client.command()
async def join(ctx):
    await ctx.send('join us Esp')


client.run(os.getenv('DTOKEN'))
