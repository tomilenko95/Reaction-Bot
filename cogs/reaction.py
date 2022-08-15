from discord.ext import commands
import discord
import random

# A list with links to reaction gifs (kiss, hug, punch and etc)
kis = ['https://cdn.discordapp.com/attachments/906658774935302227/909129371325960232/anime-kissing.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725599513485382/giphy3.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725599752564776/giphy2.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/916725600041984121/giphy.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/909129370357092382/anime-kiss3.gif',
        'https://cdn.discordapp.com/attachments/906658774935302227/909129373523804190/anime-kissing2.gif'
        ]


fuk = ['https://cdn.discordapp.com/attachments/1001737508205375558/1008126551474319432/ezgif.com-gif-maker.gif',
       'https://cdn.discordapp.com/attachments/1001737508205375558/1008128345336197160/ezgif.com-gif-maker.gif',
       'https://cdn.discordapp.com/attachments/1001737508205375558/1008130412196929607/ezgif.com-gif-maker.gif'
        ]

puts = ['https://media.discordapp.net/attachments/1003002531024228352/1008363607215591434/a9c771e756e3a920c0923a109f32c145.gif',
        'https://media.discordapp.net/attachments/1003002531024228352/1008363607538540594/b459058ae02cb62ce92c30f5be117928.gif'
        ]



class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))






    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Поцелуй")
        embed.description = f"{ctx.author.mention} поцеловал(а) {member.mention}"
        url = (random.choice(kis))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def fuck(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Поглаживание")
        embed.description = f"{ctx.author.mention} Погладил(а) {member.mention}"
        url = (random.choice(fuk))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


    @commands.command()
    async def put(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=member.color, title="Обнимашки")
        embed.description = f"{ctx.author.mention} Обнял(a) {member.mention}"
        url = (random.choice(puts))
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Reaction(bot))