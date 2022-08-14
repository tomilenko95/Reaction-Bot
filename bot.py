import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import config
import sqlite3
from discord import utils
from colorama import Fore, Back, Style
import asyncio
import discord
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

@bot.command()
async def load(ctx, extension):
    extension = extension.lower()
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')


@bot.command()
async def unload(ctx, extension):
    extension = extension.lower()
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")
 

discord.opus.load_opus()
if not discord.opus.is_loaded():
    raise RunTimeError('Opus failed to load')
 
#voice.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", **FFMPEG_OPTIONS))



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' на Boobs'))
    print('Запущен: {}'.format(bot.user.name))
    print('ID бота: {}'.format(bot.user.id))




bot.run(config.TOKEN)


