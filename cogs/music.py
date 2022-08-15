import asyncio
import discord
import youtube_dl
from discord import FFmpegPCMAudio
import discord
import json
import datetime
from discord.ext import commands
import random
from random import randint
import math
from colorama import Fore, Back, Style


with open('config.json', 'r', encoding="utf-8") as file:
	config = json.load(file)

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': False,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def p(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        guild = ctx.guild
        gname = guild.name
        clientname = config["settings"]["name"]
        embed=discord.Embed(title= "<a:7546tree:919153727913476138>Сейчас играет:", color=000000)
        embed.add_field(name='{}'.format(player.title), value='⠀', inline=False)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1001737508205375558/1008149432782561290/giphy.gif")
        
        embed.set_footer(text=f"{gname} • {clientname}")
        await ctx.send(embed=embed)
        
        


    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Не подключён к голосовому каналу.")

        ctx.voice_client.source.volume = volume / 100

        guild = ctx.guild
        gname = guild.name
        clientname = config["settings"]["name"]
        embed=discord.Embed(title= "<a:7546tree:919153727913476138>Громкость<a:7546tree:919153727913476138>", color=000000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/906658774935302227/1008123239593152602/giphy.gif")
        embed.add_field(name="Громкость была изменена", value='<:1852_volume:1008132076819718195>`{}`%'.format(volume), inline=True)
        
        embed.set_footer(text=f"{gname} • {clientname}")
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        """STOP"""

        await ctx.voice_client.disconnect()

        guild = ctx.guild
        gname = guild.name
        clientname = config["settings"]["name"]
        embed=discord.Embed(title= "<a:7546tree:919153727913476138>Остановка<a:7546tree:919153727913476138>", color=000000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/906658774935302227/1008123239593152602/giphy.gif")
        embed.add_field(name="Бот был остановлен", value="*<:pepeinshit:998978678786641981>*", inline=True)
        
        embed.set_footer(text=f"{gname} • {clientname}")
        await ctx.send(embed=embed) 

    @p.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Вы не подключены к голосовому каналу.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

def setup(client):
    client.add_cog(Music(client))
    print('Music: activated')
