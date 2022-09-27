import discord
from discord.ext import commands


description = ''''''
intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents, activity = discord.Activity(type=discord.ActivityType.watching, name=" tě!"))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


bot.run(APIKLÍČ)