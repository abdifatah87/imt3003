import discord, os
from discord.ext import commands
import aiohttp
import asyncio
import json

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready.")
    async with aiohttp.ClientSession() as session:
        channel = client.get_channel()  #fyll in drift kanal id
        while True:
            async with session.get('https://www.vg.no/') as r:
                if r.status == 200: #sjekker status paa siden
                    await channel.send('sup bro, det er abdi btw')
                    #await asyncio.sleep(10) #Waits for 10 seconds

@client.command(aliases=['ey'])
async def sup_bian(ctx):
    await ctx.send('ello')

@client.command(aliases=['what_is_security'])
async def spor(ctx):
    await ctx.send('security is a process, not a product')

@client.command()
async def hello(ctx):
    ctx.channel = client.get_channel(667785200071081985)
    await ctx.channel.send('message')

client.run(os.getenv('DTOKEN'))
