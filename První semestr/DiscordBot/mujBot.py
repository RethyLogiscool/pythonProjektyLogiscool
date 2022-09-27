from dis import dis
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ping'):
        await message.channel.send('pong')


client.run('API_KEY')