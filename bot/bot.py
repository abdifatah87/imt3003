import discord, os
from discord.ext import commands
import aiohttp
import asyncio
import json

client = commands.Bot(command_prefix = '.')

timeout = 60*10     #10 minutter timeout

@client.event
async def on_ready():
    print("bot is ready.")

async def background_task():
    await client.wait_until_ready()
    async with aiohttp.ClientSession() as session:
        channel = client.get_user('fyll inn id')     #fyll in drift kanal id
        while not client.is_closed():
            async with session.get('https://www.vg.no/') as r:
                if r.status == 200:     #sjekker status paa siden
                    await channel.send('test')
                    await asyncio.sleep(timeout)    #Waits for 10 seconds

@client.command()
async def status(ctx):
    pass    #gir status på servere

client.loop.create_task(background_task())
client.run(os.getenv('DTOKEN'))
