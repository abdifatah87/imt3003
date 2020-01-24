import discord, os
from discord.ext import commands
import requests
import json

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready.")
    errorChannel = client.get_user(249276619473027082)     #fyll in drift kanal id
    generalChannel = client.get_user(668547115341053965)
    checkApache()

    await client.logout()

def checkApache():
    r = requests.get('http://10.212.141.148')
    if r.status_code == 200:     #sjekker status paa siden

client.run(os.getenv('DTOKEN'))
