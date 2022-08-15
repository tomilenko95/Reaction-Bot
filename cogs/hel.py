import discord
import json
import datetime
from pymongo import MongoClient
from discord.ext import commands
import random
from random import randint
import math
from colorama import Fore, Back, Style



with open('config.json', 'r', encoding="utf-8") as file:
	config = json.load(file)


class hp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print(Fore.GREEN + 'Module {} is loaded'.format(self.__class__.__name__))
        print(Style.RESET_ALL)





    @commands.command()
    async def help(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        gname = guild.name
        clientname = config["settings"]["name"]
        embed=discord.Embed(title= "<a:7546tree:919153727913476138>Пожалуйста выберите категорию<a:7546tree:919153727913476138>", color=2899536)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/nVKS-mrrI3YGoI-HZZkGeBAM2FbGHRedipqXkTNO4Z8/%3Fsize%3D48/https/cdn.discordapp.com/emojis/894237267252613160.gif")
        embed.add_field(name="`#help1`", value="*<a:3496diamond:920995053491605636>Экономика*", inline=True)
        embed.add_field(name="`#help2`", value="*<a:6325squirtlehype:920994776667553833>Развлечения*", inline=False)
        embed.add_field(name="`#help3`", value="*<a:3335snowflake:920995642703224853>Разное*", inline=False)
        
        embed.set_footer(text=f"{gname} • {clientname}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(hp(bot))
