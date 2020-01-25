import discord, os, subprocess
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready.")
    #errorChannel = client.get_user(249276619473027082)     #fyll in drift kanal id
    #generalChannel = client.get_user(668547115341053965)
    checkApache()
    checkNumOfRows()
    await client.logout()

def checkApache():
    a = subprocess.check_output(['./num.sh'])
    a = a.decode().rstrip()
    if a == '2':
        print("alt er oppe")

def checkNumOfRows():
    a = subprocess.check_output(['./ant.sh'])
    a = a.decode().rstrip().replace('\n', '')[5:]
    print(a)

client.run(os.getenv('DTOKEN'))
