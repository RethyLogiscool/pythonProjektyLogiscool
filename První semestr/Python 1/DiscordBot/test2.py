# This example requires the 'members' and 'message_content' privileged intents to function.

import string
from attr import field
import discord
from discord.ext import commands
import random,sys,platform
import psutil, os
from time import time,ctime
from datetime import timedelta
from apiModule import *
startTime = time()

def getUptime():
    return time() - startTime

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
    """Counting."""
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    """Just a ping pong."""
    await ctx.send("pong!")

@bot.command()
async def table(ctx, message: str):
    """Show demonstration table."""
    e = discord.Embed(title=f"**Logiscool bot**", color=0xFF0000,timestamp = ctx.message.created_at)
    e.add_field(name=f'**Ahoj 👋**', value=f"{message}",inline=False)
    await ctx.send(embed=e)  


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)



@bot.command()
async def hi(ctx):
    """Just say hi."""
    await ctx.author.add_roles(ctx.guild.get_role(424887745199210497))
    


@bot.command()
async def joke(ctx):
    """Generate random joke."""
    resp = connectApi("https://v2.jokeapi.dev/joke/Any").json()
    type = resp["type"]
    if(type == "single"):
        msg = resp["joke"]
    else:
        msg = resp["setup"]
        msg += " ... "
        msg += resp["delivery"]

    if(True in resp["flags"].values()):
        await ctx.author.send(msg)
        await ctx.send("Máš to v DM 🤫")
    else: 
        await ctx.send(msg)

@bot.command()
async def about(ctx):
    """About stats."""
 
    list = [
        ("**Ahoj 👋**","Jsem Discordí bot 🤖 Logiscool a vznikl jsem v rámci kurzu **Programování v Pythonu**. ",False),
        ("**🐍 Python:**", f"Python v{sys.version_info[0]}" ,True),
        ("**📚 Knihovna:**", f"Discord.py v{discord.__version__}" ,True),
        ("**🖥 OS:**", f"macOS {platform.mac_ver()[0]}" ,True),
        ("**🕑 Uptime:**", f"{str(timedelta(seconds=getUptime()))[:-7]}s" ,True),
        ("**👨🏻‍💻 Autor:**", "<@168419622293471232>" ,True),
        ("**📈 Využití procesoru:**", f"{psutil.cpu_percent()} %" ,True),
        ("**💾 Využití paměti:**", f"{psutil.virtual_memory().percent} %" ,True)
        ]

    await ctx.send(embed=generateTable(ctx,"**Logiscool bot**", 0x90550, list))  

def generateTable(ctx,title,color,field_list):
    embed = discord.Embed(title=title,color=color,timestamp=ctx.message.created_at)
    for nadpis, hodnota, inline in field_list:
        embed.add_field(name=nadpis,value=hodnota,inline=inline)
    return embed















































bot.run('OTc4Njk4MDkyNDY5NjgyMjU2.GmfD3Q.Ls6x1lrY0-5GR9891COt-UPsLOZNfeaPBiJtqE')